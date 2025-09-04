from pydantic import BaseModel, EmailStr

# Request schema for creating a user
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Response schema (what we send back to client)
class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True  # allows SQLAlchemy model -> Pydantic conversion
