from fastapi import APIRouter
from users.schemas import UserCreate, UserResponse
from users.services import create_user

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate):
    return create_user(user.email, user.password)
