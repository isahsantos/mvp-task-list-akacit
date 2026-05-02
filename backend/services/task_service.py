from sqlalchemy.orm import Session
import schemas
from repositories import task_repository
from services.ai_service import generate_task_with_ai

def create_task(db: Session, task: schemas.TaskCreate):
    return task_repository.create_task(db, task)

def list_tasks(db: Session):
    return task_repository.list_tasks(db)

def get_task(db: Session, task_id: int):
    return task_repository.get_task_by_id(db, task_id)

def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate):
    return task_repository.update_task(db, task_id, task_update)

def delete_task(db: Session, task_id: int):
    return task_repository.delete_task(db, task_id)

def complete_task(db: Session, task_id: int):
    return task_repository.complete_task(db, task_id)

def generate_ai_task(title: str):
    return generate_task_with_ai(title)