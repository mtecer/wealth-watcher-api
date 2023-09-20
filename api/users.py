from fastapi import APIRouter

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
    return USERS