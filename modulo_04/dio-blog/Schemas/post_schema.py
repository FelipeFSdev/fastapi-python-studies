from datetime import datetime

from pydantic import BaseModel


class PostIn(BaseModel):
    title: str
    date: datetime = datetime.now()
    active: bool = False
