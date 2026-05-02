from sqlalchemy.orm import Session
import models
import schemas

def create_task(db: Session, task: schemas.TaskCreate):
    new_task = models.Task(**task.model_dump())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def list_tasks(db: Session):
    return db.query(models.Task).all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate):
    task = get_task_by_id(db, task_id)

    if not task:
        return None

    update_data = task_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)

    if not task:
        return None

    db.delete(task)
    db.commit()
    return task

def complete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)

    if not task:
        return None

    task.completed = True
    task.status = "concluida"

    db.commit()
    db.refresh(task)
    return task