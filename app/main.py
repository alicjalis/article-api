from fastapi import FastAPI

app = FastAPI(title="Article API")

@app.get("/")
def root():
    return {"message": "Article API is running"}