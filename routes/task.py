from typing import Annotated
from fastapi import APIRouter, Depends
from models.task import Task
from deps import RepoDep

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
def get_tasks(team_id: int | None = None, repo: RepoDep = None) -> list[Task]:
    return repo.task_repo.getByTeamId(team_id)

@router.post("/")
def add_task(task: Task, repo: RepoDep):
    id = repo.task_repo.add(task)
    return {"id": id}

@router.get("/{id}")
def get_task(id: int, repo: RepoDep):
    result = repo.task_repo.get(id)
    return result

@router.put("/{id}")
def change_task(id: int, task: Task, repo: RepoDep):
    updated = repo.task_repo.update(id, task)
    return {"updated": updated}

@router.delete("/{id}")
def delete_task(id: int, repo: RepoDep):
    deleted = repo.task_repo.delete(id)
    return {"deleted": deleted}
    
