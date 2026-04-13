from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from app.db.database import Base
from datetime import datetime, timezone

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))