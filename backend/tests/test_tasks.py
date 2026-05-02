import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

import models
from database import Base
from main import app
from controllers.task_controller import get_db


# ---------------------------------------------------------------------------
# Configuração do banco de testes (SQLite em memória)
# ---------------------------------------------------------------------------
TEST_DATABASE_URL = "sqlite:///:memory:"

engine_test = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # garante a mesma conexão entre threads do TestClient
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine_test,
)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------
@pytest.fixture(autouse=True)
def setup_database():
    """Cria o schema antes de cada teste e dropa depois.
    Garante isolamento total entre testes."""
    Base.metadata.create_all(bind=engine_test)
    yield
    Base.metadata.drop_all(bind=engine_test)


@pytest.fixture
def create_task():
    """Helper para criar tasks com payload customizável."""
    def _create(**overrides):
        payload = {
            "title": "Task padrão",
            "description": "Descrição padrão",
            "status": "pendente",
            "priority": "media",
            "completed": False,
            **overrides,
        }
        response = client.post("/tasks/", json=payload)
        assert response.status_code in (200, 201), f"Falha ao criar task: {response.text}"
        return response.json()
    return _create


# ---------------------------------------------------------------------------
# Happy path
# ---------------------------------------------------------------------------
def test_create_task():
    response = client.post("/tasks/", json={
        "title": "Estudar FastAPI",
        "description": "Criar CRUD com testes",
        "status": "pendente",
        "priority": "alta",
        "completed": False,
    })

    assert response.status_code in (200, 201)

    data = response.json()
    assert data["title"] == "Estudar FastAPI"
    assert data["description"] == "Criar CRUD com testes"
    assert data["priority"] == "alta"
    assert data["completed"] is False
    assert "id" in data


def test_list_tasks(create_task):
    create_task(title="Task 1")
    create_task(title="Task 2")
    create_task(title="Task 3")

    response = client.get("/tasks/")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 3


def test_list_tasks_empty():
    response = client.get("/tasks/")

    assert response.status_code == 200
    assert response.json() == []


def test_get_task_by_id(create_task):
    task = create_task(title="Buscar por ID")
    task_id = task["id"]

    response = client.get(f"/tasks/{task_id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == task_id
    assert data["title"] == "Buscar por ID"


def test_update_task(create_task):
    task = create_task(title="Tarefa antiga", priority="baixa")
    task_id = task["id"]

    response = client.put(f"/tasks/{task_id}", json={
        "title": "Tarefa atualizada",
        "priority": "alta",
    })
    data = response.json()

    assert response.status_code == 200
    assert data["title"] == "Tarefa atualizada"
    assert data["priority"] == "alta"


def test_complete_task(create_task):
    task = create_task(title="Concluir tarefa")
    task_id = task["id"]

    response = client.patch(f"/tasks/{task_id}/complete")
    data = response.json()

    assert response.status_code == 200
    assert data["completed"] is True
    assert data["status"] == "concluida"


def test_delete_task(create_task):
    task = create_task(title="Excluir tarefa")
    task_id = task["id"]

    response = client.delete(f"/tasks/{task_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Tarefa excluída com sucesso"

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404


# ---------------------------------------------------------------------------
# Caminhos infelizes
# ---------------------------------------------------------------------------
def test_get_task_not_found():
    response = client.get("/tasks/99999")
    assert response.status_code == 404


def test_update_task_not_found():
    response = client.put("/tasks/99999", json={"title": "qualquer"})
    assert response.status_code == 404


def test_delete_task_not_found():
    response = client.delete("/tasks/99999")
    assert response.status_code == 404


def test_create_task_invalid_payload():
    # falta campos obrigatórios
    response = client.post("/tasks/", json={"description": "sem título"})
    assert response.status_code == 422


def test_complete_task_not_found():
    response = client.patch("/tasks/99999/complete")
    assert response.status_code == 404

