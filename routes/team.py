from fastapi import APIRouter
from models.team import Team
from repositories.team import TeamRepo

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.get("/")
def get_teams() -> list[Team]:
    return TeamRepo.getAll()

@router.post("/")
def add_team(team: Team):
    id = TeamRepo.add(team)
    return {"id": id}

@router.put("/{id}")
def change_team(id: int, team: Team):
    updated = TeamRepo.update(id, team)
    return {"updated": updated}

@router.delete("/{id}")
def delete_team(id: int):
    deleted = TeamRepo.delete(id)
    return {"deleted": deleted}
