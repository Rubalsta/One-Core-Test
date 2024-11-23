from fastapi import FastAPI
from app.routers import users
from app.database import engine, SessionLocal
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(users.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
