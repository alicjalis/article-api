from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.user import User
from app.schemas.article import ArticleCreate, ArticleUpdate, ArticleOut
from app.services.article_service import (
    create_article, get_articles, get_article, update_article, delete_article, bulk_create_articles
)
from app.core.deps import get_current_user

router = APIRouter(prefix="/articles", tags=["articles"])

@router.post("/bulk", response_model=list[ArticleOut], status_code=status.HTTP_201_CREATED)
def bulk_import(
    articles_data: list[ArticleCreate],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return bulk_create_articles(db, articles_data, author_id=current_user.id)


@router.post("/", response_model=ArticleOut, status_code=status.HTTP_201_CREATED)
def create(
    data: ArticleCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_article(db, data, author_id=current_user.id)


@router.get("/", response_model=list[ArticleOut])
def list_articles(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return get_articles(db, skip=skip, limit=limit)


@router.get("/{article_id}", response_model=ArticleOut)
def get_one(article_id: int, db: Session = Depends(get_db)):
    article = get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    return article


@router.patch("/{article_id}", response_model=ArticleOut)
def update(
    article_id: int,
    data: ArticleUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    article = get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    if article.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not your article")
    return update_article(db, article, data)


@router.delete("/{article_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    article_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    article = get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found")
    if article.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not your article")
    delete_article(db, article)


