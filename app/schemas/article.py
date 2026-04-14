from pydantic import BaseModel, field_validator
from datetime import datetime


class ArticleCreate(BaseModel):
    title: str
    content: str

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("Title cannot be empty")
        return v.strip()

    @field_validator("content")
    @classmethod
    def content_min_length(cls, v: str) -> str:
        if len(v.strip()) < 10:
            raise ValueError("Content must be at least 10 characters")
        return v.strip()


class ArticleUpdate(BaseModel):
    title: str | None = None
    content: str | None = None

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str | None) -> str | None:
        if v is not None and not v.strip():
            raise ValueError("Title cannot be empty")
        return v.strip() if v else v

    @field_validator("content")
    @classmethod
    def content_min_length(cls, v: str | None) -> str | None:
        if v is not None and len(v.strip()) < 10:
            raise ValueError("Content must be at least 10 characters")
        return v.strip() if v else v


class ArticleOut(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    author_id: int

    model_config = {"from_attributes": True}