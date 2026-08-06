from fastapi import FastAPI
from app.routers.notes import router as notes_router
from app.routers.users import router as users_router

app = FastAPI(
    title="Notes API",
    version="1.0.0"
)

app.include_router(notes_router)
app.include_router(users_router)

@app.get("/")
def root():
    return {"message": "Welcome to Notes API"}