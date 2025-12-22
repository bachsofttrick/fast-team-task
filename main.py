from fastapi import FastAPI
from routes.team import router as teamRouter
from routes.task import router as taskRouter

app = FastAPI()
app.include_router(teamRouter)
app.include_router(taskRouter)