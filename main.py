from typing import Annotated
from fastapi import FastAPI, Path, Header
from pydantic import BaseModel

class Team(BaseModel):
    id: int
    name: str

teams = []
tasks = []
count = 1

team1 = Team(id=1, name='test')
teams.append(team1)

app = FastAPI()

@app.get("/teams")
def get_teams() -> list[Team]:
    return teams

@app.post("/teams")
def add_team(team: Team):
    global count
    count += 1
    team.id = count
    teams.append(team)
    return {"added": team}

@app.put("/teams/{id}")
def change_team(id: int, team: Team):
    for old_team in teams:
        if old_team.id == id:
            old_team.name = team.name
            return {"updated": old_team}
    
    return {"updated": 0}

@app.delete("/teams/{id}")
def delete_team(id: Annotated[int, Path(description='delete a certain team')]):
    global teams
    deleted = False
    new_teams = []
    for old_team in teams:
        if old_team.id != id:
            new_teams.append(old_team)
        else:
            deleted = True
    
    teams = new_teams
    return {"deleted": 0 if not deleted else id}
