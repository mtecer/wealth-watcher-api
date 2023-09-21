import json

from fastapi import APIRouter
from pydantic import BaseModel
from uuid import uuid4

from config import read_users, write_users

class User(BaseModel):
    id: uuid4
    user_name: str = None
    name: str | None = None

router = APIRouter()

USERS = [
    {
        "id": "91cf6a87-c449-4940-b10d-5c792e03657d",
        "user_name": "user_1",
        "name": "User One"
    },
    {
        "id": "5d854cd3-2920-495a-8b8e-f5e4887e7db8",
        "user_name": "user_2",
        "name": "User Two"
    },
    {
        "id": "d98acc31-223b-46e7-9664-dea41e8b091c",
        "user_name": "user_3",
        "name": "User Three"
    }
]

@router.get("/api/users")
async def get_users():
    return read_users()

@router.get("/api/users/{user_name}")
async def get_user(user_name: str):
    return read_users()

@router.post("/api/users/")
async def craete_user(user: User):
    users = read_users()
    users.append(json.loads(user.model_dump_json()))
    write_users(users)
    return user
