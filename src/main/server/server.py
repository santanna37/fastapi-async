from fastapi import FastAPI
from src.main.routes.route_pessoas import pessoas_routes

app = FastAPI()
app.include_router(pessoas_routes)