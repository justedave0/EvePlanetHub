from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel

router = APIRouter()

# Sample user model
class User(BaseModel):
    id: int
    name: str
    email: str

# In-memory storage (replace with database in production)
fake_users_db = [
    User(id=1, name="John Doe", email="john@example.com"),
    User(id=2, name="Jane Smith", email="jane@example.com")
]

@router.get("/users", response_model=List[User])
async def get_users():
    return fake_users_db

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    for user in fake_users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")