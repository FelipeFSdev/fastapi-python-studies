from datetime import datetime
from sqlmodel import Field, SQLModel


class Post(SQLModel, table=True):
    id: int | None = Field(primary_key=True, default=None)
    title: str = Field(unique=True, nullable=False, max_length=150)
    content: str = Field(nullable=False)
    published_at: datetime | None = Field(nullable=True, default=None)
    is_publish: bool = False
