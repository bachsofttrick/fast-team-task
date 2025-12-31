import strawberry

@strawberry.type
class Team():
    id: int
    name: str

@strawberry.input
class TeamInput(Team):
    pass