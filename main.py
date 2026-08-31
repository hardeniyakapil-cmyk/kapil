
from fastapi import FastAPI,HTTPException
from database.connection import connect_database
from routes.auth import router as auth_router
from routes.get_users import router as get_user

connect_database()

app=FastAPI(
    title="Tour and Travel API",
    version="1.0.0"
)

@app.get("/health")
async def health_check():
    print("Health check endpoint called")
    return {"status": "ok✅"}

app.include_router(auth_router)
app.include_router(get_user)


