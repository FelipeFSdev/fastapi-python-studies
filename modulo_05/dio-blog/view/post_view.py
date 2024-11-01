from datetime import datetime
from pydantic import BaseModel


class PostOutput(BaseModel):
    id: int
    title: str
    content: str
    published_at: datetime | None
