from contextlib import asynccontextmanager
from fastapi import FastAPI
from controller import post_controller
from database.engine import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(post_controller.router)
