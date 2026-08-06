from fastapi import FastAPI
from app.routers.notes import router

app = FastAPI(
    title="Notes API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to Notes API"}