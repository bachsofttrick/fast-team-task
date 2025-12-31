# Fast Team Task
Team Tasks API with FastAPI and GraphQL 

## Todo
- [x] Implement 4 API with FastAPI (uvicorn) with in-memory database first:
  - [x] POST /teams - create a team
  - [x] GET /teams - list all teams
  - [x] POST /tasks - create a task
  - [x] GET /tasks?team_id= - list tasks for a team
```
team: {
  id: int
  name: str
}
task: {
  id: int
  team_id: Fkey(team.id)
  title: str
  completed: bool
}
```
- [x] Implement /graphql with strawberry-graphql
  - Queries
  - [x] teams: [Team]
  - [x] tasks(teamId: Int): [Task]  
  - Mutations
  - [x] createTeam(name: String!): Team
  - [x] createTask(teamId: Int!, title: String!): Task
- [x] Extra: Add Dependency Injection
```
def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
def get_team_repo(db: Session = Depends(get_db)) -> TeamRepo:
  return TeamRepo(db)
RepoDep = Annotated[TeamRepo, Depends(get_team_repo)]
def get_teams(repo: RepoDep):
```
- [ ] Extra: Implement SQLite with SQLAlchemy
  - [ ] Migration with Alembic
