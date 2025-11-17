from fastapi import FastAPI
from pydantic import BaseModel

class Team(BaseModel):
    id: int
    name: str

teams = []
tasks = []

team1 = Team(id=1, name='test')
teams.append(team1)

app = FastAPI()

@app.get("/teams")
def get_teams():
    return teams

@app.post("/teams")
def add_team(team: Team):
    count = len(teams)
    team.id = count + 1
    teams.append(team)
    return {"status": "OK"}

@app.put("/teams/{id}")
def change_team(id: int, team: Team):
    for old_team in teams:
        if old_team.id == id:
            old_team.name = team.name
    
    return {"status": "OK"}

@app.delete("/teams/{id}")
def delete_team(id: int):
    global teams
    new_teams = []
    for old_team in teams:
        if old_team.id != id:
            new_teams.append(old_team)
    
    teams = new_teams
    return {"status": "OK"}
