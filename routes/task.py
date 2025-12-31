from fastapi import APIRouter
from models.task import Task
from repositories.task import TaskRepo

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/")
def get_tasks(team_id: int | None = None) -> list[Task]:
    return TaskRepo.getByTeamId(team_id)

@router.post("/")
def add_task(task: Task):
    id = TaskRepo.add(task)
    return {"id": id}

@router.get("/{id}")
def get_task(id: int):
    result = TaskRepo.get(id)
    return result

@router.put("/{id}")
def change_task(id: int, task: Task):
    updated = TaskRepo.update(id, task)
    return {"updated": updated}

@router.delete("/{id}")
def delete_task(id: int):
    deleted = TaskRepo.delete(id)
    return {"deleted": deleted}
    
