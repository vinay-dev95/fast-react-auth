from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserCreate, UserResponse
from services.user_service import create_user
from db.session import get_db

router = APIRouter()

@router.post("/", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db, user)
    if not db_user:
        raise HTTPException(status_code=400, detail="User already exists")
    return db_user
