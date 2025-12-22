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
- [ ] Implement /graphql with strawberry-graphql
  - Queries
  - [ ] teams: [Team]
  - [ ] tasks(teamId: Int): [Task]  
  - Mutations
  - [ ] createTeam(name: String!): Team
  - [ ] createTask(teamId: Int!, title: String!): Task
- [ ] Extra: Implement SQLite with SQLAlchemy
  - [ ] Migration with Alembic
