from sqlalchemy.orm import Session
from app.models.article import Article
from app.schemas.article import ArticleCreate, ArticleUpdate
from app.services.notification_service import notify_subscribers


def create_article(db: Session, data: ArticleCreate, author_id: int) -> Article:
    article = Article(
        title=data.title,
        content=data.content,
        author_id=author_id
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    
    from app.models.user import User
    author = db.query(User).filter(User.id == author_id).first()
    notify_subscribers(db, article.title, author.username)

    return article


def get_articles(db: Session, skip: int = 0, limit: int = 20) -> list[Article]:
    return db.query(Article).offset(skip).limit(limit).all()


def get_article(db: Session, article_id: int) -> Article | None:
    return db.query(Article).filter(Article.id == article_id).first()


def update_article(db: Session, article: Article, data: ArticleUpdate) -> Article:
    if data.title is not None:
        article.title = data.title
    if data.content is not None:
        article.content = data.content
    db.commit()
    db.refresh(article)
    return article


def delete_article(db: Session, article: Article) -> None:
    db.delete(article)
    db.commit()