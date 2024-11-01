from datetime import datetime
from typing import Annotated

from fastapi import FastAPI, status, Cookie, Response, APIRouter
from Schemas.post_schema import PostIn
from View.post_view import PostOut

router = APIRouter(prefix="/posts")

fake_db = [
    {"title": f"Criando aplicação com Django",
        "date": datetime.now(), "active": False},
    {"title": f"Criando aplicação com FastAPI",
        "date": datetime.now(), "active": True},
    {"title": f"Criando aplicação com Flask",
        "date": datetime.now(), "active": True},
    {"title": f"Criando aplicação com Starlett",
        "date": datetime.now(), "active": True},
]


@router.get("/{framework}", response_model=PostOut, status_code=status.HTTP_200_OK)
def read_posts(framework: str):
    return {"posts": [
        {"title": f"Criando aplicação com {framework}", "date": datetime.now()},
        {"title": f"Criando aplicação com {framework}", "date": datetime.now()},
    ]}


@router.get("/", response_model=list[PostOut], status_code=status.HTTP_200_OK)
def read_post(
        res: Response,
        limit: int, skip: int = 0,
        active: bool = True,
        ads_id: Annotated[str | None, Cookie()] = None):
    res.set_cookie(key="user", value="user@email.com")
    active_posts = []
    for post in fake_db:
        if (len(active_posts) == limit):
            break
        if (post["active"] == active):
            active_posts.append(post)

    print(f"Cookie: {ads_id}")
    return active_posts


@router.post("/", response_model=PostOut, status_code=status.HTTP_201_CREATED)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post
