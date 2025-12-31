import typing
import strawberry
from strawberry.fastapi import GraphQLRouter
from models.team import Team, TeamInput
from models.task import Task, TaskInput
from deps import dependency_context
from deps import repo_for_graphql as repo

@strawberry.type
class Query:
    @strawberry.field
    def teams(self, info: strawberry.Info) -> list[Team]:
        return repo(info).team_repo.getAll()

    @strawberry.field
    def team(self, id: int, info: strawberry.Info) -> Team | None:
        return repo(info).context.team_repo.get(id)

    @strawberry.field
    def tasks_all(self, info: strawberry.Info) -> list[Task]:
        return repo(info).task_repo.getByTeamId(None)
    
    @strawberry.field
    def tasks(self, team_id: int, info: strawberry.Info) -> list[Task]:
        return repo(info).task_repo.getByTeamId(team_id)

    @strawberry.field
    def task(self, id: int, info: strawberry.Info) -> Task | None:
        return repo(info).task_repo.get(id)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_team(self, team: TeamInput, info: strawberry.Info) -> int:
        id = repo(info).team_repo.add(team)
        return id
        
    @strawberry.mutation
    def change_team(self, id: int, team: TeamInput, info: strawberry.Info) -> bool:
        updated = repo(info).team_repo.update(id, team)
        return updated  

    @strawberry.mutation
    def delete_team(self, id: int, info: strawberry.Info) -> bool:
        deleted = repo(info).team_repo.delete(id)
        return deleted
        
    @strawberry.mutation
    def add_task(self, task: TaskInput, info: strawberry.Info) -> int:
        id = repo(info).task_repo.add(task)
        return id
        
    @strawberry.mutation
    def change_task(self, id: int, task: TaskInput, info: strawberry.Info) -> bool:
        updated = repo(info).task_repo.update(id, task)
        return updated  

    @strawberry.mutation
    def delete_task(self, id: int, info: strawberry.Info) -> bool:
        deleted = repo(info).task_repo.delete(id)
        return deleted

schema = strawberry.Schema(query=Query,mutation=Mutation)
graphql_route = GraphQLRouter(schema, context_getter=dependency_context)
