from fastapi import FastAPI
from app.db.database import Base, engine
from app.api import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Article API")

app.include_router(auth.router)