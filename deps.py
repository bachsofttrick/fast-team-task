from typing import Annotated
from fastapi import Depends
from repositories.team import TeamRepo
from repositories.task import TaskRepo
from strawberry.fastapi import BaseContext
import strawberry

class DependencyContext(BaseContext):
    def __init__(self):
        self.team_repo = self.get_team_repo()
        self.task_repo = self.get_task_repo()
    
    def get_team_repo(self) -> TeamRepo:
        return TeamRepo()

    def get_task_repo(self) -> TaskRepo:
        return TaskRepo()

RepoDep = Annotated[DependencyContext, Depends(DependencyContext)]

def dependency_context(custom_context=Depends(DependencyContext)):
    return custom_context

def repo_for_graphql(info: strawberry.Info) -> DependencyContext:
    return info.context
