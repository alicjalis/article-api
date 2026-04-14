from fastapi import FastAPI
from app.db.database import Base, engine
from app.api import auth, articles, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Article API")

app.include_router(auth.router)
app.include_router(articles.router)
app.include_router(users.router)