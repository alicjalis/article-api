from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.db.database import Base, engine
from app.api import auth, articles, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Article API")


@app.get("/")
def root():
    return {"message": "Article API is running", "docs": "/docs"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": error["loc"][-1],
            "message": error["msg"]
        })
    return JSONResponse(
        status_code=422,
        content={"detail": errors}
    )

app.include_router(auth.router)
app.include_router(articles.router)
app.include_router(users.router)