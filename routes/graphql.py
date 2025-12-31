import typing
import strawberry
from strawberry.fastapi import GraphQLRouter
from models.team import Team, TeamInput
from models.task import Task, TaskInput
from repositories.team import TeamRepo
from repositories.task import TaskRepo

@strawberry.type
class Query:
    @strawberry.field
    def teams(self) -> list[Team]:
        return TeamRepo.getAll()

    @strawberry.field
    def team(self, id: int) -> Team | None:
        return TeamRepo.get(id)

    @strawberry.field
    def tasks_all(self) -> list[Task]:
        return TaskRepo.getByTeamId(None)
    
    @strawberry.field
    def tasks(self, team_id: int) -> list[Task]:
        return TaskRepo.getByTeamId(team_id)

    @strawberry.field
    def task(self, id: int) -> Task | None:
        return TaskRepo.get(id)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_team(self, team: TeamInput) -> int:
        id = TeamRepo.add(team)
        return id
        
    @strawberry.mutation
    def change_team(self, id: int, team: TeamInput) -> bool:
        updated = TeamRepo.update(id, team)
        return updated  

    @strawberry.mutation
    def delete_team(self, id: int) -> bool:
        deleted = TeamRepo.delete(id)
        return deleted
        
    @strawberry.mutation
    def add_task(self, task: TaskInput) -> int:
        id = TaskRepo.add(task)
        return id
        
    @strawberry.mutation
    def change_task(self, id: int, task: TaskInput) -> bool:
        updated = TaskRepo.update(id, task)
        return updated  

    @strawberry.mutation
    def delete_task(self, id: int) -> bool:
        deleted = TaskRepo.delete(id)
        return deleted

schema = strawberry.Schema(query=Query,mutation=Mutation)
graphql_route = GraphQLRouter(schema)
