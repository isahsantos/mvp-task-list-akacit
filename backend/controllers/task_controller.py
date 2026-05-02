from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import schemas
from database import SessionLocal
from services import task_service

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task)

@router.get("/", response_model=List[schemas.TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return task_service.list_tasks(db)

@router.get("/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return task

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = task_service.update_task(db, task_id, task_update)

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.delete_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return {"message": "Tarefa excluída com sucesso"}

@router.patch("/{task_id}/complete", response_model=schemas.TaskResponse)
def complete_task(task_id: int, db: Session = Depends(get_db)):
    task = task_service.complete_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

    return task

@router.post("/generate-ai", response_model=schemas.AIGenerateResponse)
def generate_ai_task(request: schemas.AIGenerateRequest):
    return task_service.generate_ai_task(request.title)