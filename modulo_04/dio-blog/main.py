from fastapi import FastAPI

from Controllers import post_controller

app = FastAPI()
app.include_router(post_controller.router)
