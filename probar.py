from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User

def list_users():
    db: Session = SessionLocal()
    users = db.query(User).all()
    for user in users:
        print(user.username)

if __name__ == "__main__":
    list_users()
