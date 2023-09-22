import json

from fastapi import APIRouter
from pydantic import BaseModel, Field, PrivateAttr
from uuid import uuid4

from config import read_users, write_users

def generate_uuid4() -> str:
    return str(uuid4())

class User(BaseModel):
    # id: uuid4 = Field(default_factory=get_new_uuid)
    # _id: uuid4 = PrivateAttr(default_factory=lambda: uuid4().hex)
    _id: uuid4 = PrivateAttr(default_factory=generate_uuid4)
    user_name: str = None
    name: str | None = None

    def model_dump_dict(self):
        return {
            "id": self._id,
            "user_name": self.user_name,
            "name": self.name
        }

router = APIRouter()

# USERS = [
#     {
#         "id": "91cf6a87-c449-4940-b10d-5c792e03657d",
#         "user_name": "user_1",
#         "name": "User One"
#     },
#     {
#         "id": "5d854cd3-2920-495a-8b8e-f5e4887e7db8",
#         "user_name": "user_2",
#         "name": "User Two"
#     },
#     {
#         "id": "d98acc31-223b-46e7-9664-dea41e8b091c",
#         "user_name": "user_3",
#         "name": "User Three"
#     }
# ]

# Get all users
@router.get("/api/users", status_code=200)
async def get_users():
    return read_users()

# Get user by user_name
@router.get("/api/users/{user_name}", status_code=200)
async def get_user(*, user_name: str):
    users = read_users()
    result = [ user for user in users if user["user_name"] == user_name ]
    return result if result else []

# Seaerch a user
@router.get("/api/users/search/", status_code=200)
async def search_user(keyword: str | None = None):
    users = read_users()
    result = [ user for user in users if keyword.lower() in user["user_name"].lower() ]
    return result

# Create a user
@router.post("/api/users/", status_code=201)
async def create_user(user: User):
    users = read_users()
    # users.append({
    #     # "id": str(user._id),
    #     "id": user._id,
    #     "user_name": user.user_name,
    #     "name": user.name
    # })
    users.append(user.model_dump_dict())
    # print(user)
    # print(user.model_dump_json())
    # print(user.model_dump())
    # print(user.model_dump_dict())
    write_users(users)
    # return user
    return user.model_dump_dict()

# Delete user by user_name
@router.delete("/api/users/{user_name}", status_code=204)
async def delete_user(*, user_name: str):
    users = read_users()
    result = [ user for user in users if user["user_name"] != user_name ]
    write_users(result)
    # return result

# Update user by user id
