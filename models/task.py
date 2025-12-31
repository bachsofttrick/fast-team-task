import strawberry

@strawberry.type
class Task():
    id: int
    team_id: int = 1
    title: str
    completed: bool = False

@strawberry.input
class TaskInput(Task):
    pass