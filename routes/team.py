from typing import Annotated
from fastapi import APIRouter, Depends
from models.team import Team
from repositories.team import TeamRepo
from deps import RepoDep

router = APIRouter(prefix="/teams", tags=["Teams"])

@router.get("/")
def get_teams(repo: RepoDep) -> list[Team]:
    return repo.team_repo.getAll()

@router.post("/")
def add_team(team: Team, repo: RepoDep):
    id = repo.team_repo.add(team)
    return {"id": id}

@router.get("/{id}")
def get_team(id: int, repo: RepoDep):
    result = repo.team_repo.get(id)
    return result

@router.put("/{id}")
def change_team(id: int, team: Team, repo: RepoDep):
    updated = repo.team_repo.update(id, team)
    return {"updated": updated}

@router.delete("/{id}")
def delete_team(id: int, repo: RepoDep):
    deleted = repo.team_repo.delete(id)
    return {"deleted": deleted}
