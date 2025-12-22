from pydantic import BaseModel

class Task(BaseModel):
    id: int
    team_id: int = 1
    title: str
    completed: bool = False