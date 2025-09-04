from fastapi import HTTPException
# from app.users.models import users_db
# from app.core.security import hash_password

from users.models import user_db as users_db
from core.security import hash_password

def create_user(email: str, password: str):
    if email in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[email] = hash_password(password)
    return {"email": email, "msg": "Signup successful"}
