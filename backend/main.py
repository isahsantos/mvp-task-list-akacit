from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine
from controllers import task_controller

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task AI CRUD",
    description="MVP de CRUD de tarefas com IA generativa",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(task_controller.router)

@app.get("/")
def home():
    return {"message": "API Task AI CRUD funcionando"}