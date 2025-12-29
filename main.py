from fastapi import FastAPI
from routes.team import router as teamRouter
from routes.task import router as taskRouter
from routes.graphql import graphql_route as graphqlRoute

app = FastAPI()
app.include_router(teamRouter)
app.include_router(taskRouter)
app.include_router(graphqlRoute, prefix='/graphql')
