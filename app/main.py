from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app import models, schemas, database, security
from app.config import ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta
from app.database import engine,SessionLocal
from app.routers import users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
