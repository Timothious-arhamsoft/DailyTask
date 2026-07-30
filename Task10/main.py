from fastapi import FastAPI


# Task 1: fastapi uvicorn
app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello FastAPI!"}