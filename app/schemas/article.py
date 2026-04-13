from pydantic import BaseModel
from datetime import datetime


class ArticleCreate(BaseModel):
    title: str
    content: str


class ArticleUpdate(BaseModel):
    title: str | None = None
    content: str | None = None


class ArticleOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    author_id: int

    model_config = {"from_attributes": True}