# Checking Docker
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.notes import router as notes_router
from app.routers.users import router as users_router
from app.routers.auth import router as auth_router
from app.routers.admin import router as admin_router

app = FastAPI(
    title="Notes API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://localhost:5174",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(notes_router)
app.include_router(users_router)
app.include_router(auth_router)
app.include_router(admin_router)

@app.get("/")
def root():
    return {"message": "Welcome to Notes API"}