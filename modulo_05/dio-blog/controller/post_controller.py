from fastapi import FastAPI, APIRouter, HTTPException
from sqlmodel import select
from schema.post_schema import PostInput
from view.post_view import PostOutput
from database.session import SessionDep
from model.post_model import Post


router = APIRouter(prefix="/posts")


@router.get("/", response_model=list[PostOutput], status_code=200)
def list_posts(
        session: SessionDep,
        limit: int,
        skip: int = 0):
    posts = session.exec(select(Post).offset(skip).limit(limit)).all()

    return posts


@router.get("/{post_id}", response_model=PostOutput, status_code=200)
def list_one_post(session: SessionDep, post_id: int):
    post = session.get(Post, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("/", response_model=PostOutput, status_code=201)
def create_post(body: PostInput, session: SessionDep):
    new_post = Post(title=body.title,
                    content=body.content,
                    published_at=body.published_at,
                    is_publish=body.published,)

    session.add(new_post)
    session.commit()
    session.refresh(new_post)

    return body
