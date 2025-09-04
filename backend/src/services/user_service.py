# backend/src/services/user_service.py
from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """Hash a plain password using bcrypt."""
    return pwd_context.hash(password)

def create_user(db: Session, user: UserCreate):
    """Create a new user in the database."""
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        return None
    new_user = User(
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
