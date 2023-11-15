# import json

from fastapi import APIRouter, Query, Depends
# from pathlib import Path
from pydantic import BaseModel, Field, PrivateAttr
from sqlmodel import Session, select
# from typing import Annotated
from uuid import uuid4

# from app.config import users_datafile, sqlite_url
from app.database import engine
from app.models import User, UserUpdate

def get_session():
    with Session(engine) as session:
        yield session

def generate_uuid4() -> str:
    return str(uuid4())

class UserBase(BaseModel):
    _id: uuid4 = PrivateAttr(default_factory=generate_uuid4)
    username: str = Field(default=None, title="Login credentials - username", max_length=30)
    password: str = None
    # first_name: str = None
    # middle_name: str | None = None
    # last_name: str = None
    # email: str = None
    # phone_number: str | None = None
    # address: str | None = Field(default=None, title="User's address", max_length=100)
    # birth_date: str = None
    # timestamp: str = None
    # tags: list[str] = []
    # tags: set[str] = []

# def read_users():
#     users = json.loads(users_datafile.read_text())
#     return users

# def write_users(users: list[dict]):
#     users_datafile.write_text(json.dumps(users, indent=4))

router = APIRouter()

# def create_users():
#     user_1 = User(username="user_1", password="password123")
#     user_2 = User(username="user_2", password="password456")

#     with Session(engine) as session:
#         session.add(user_1)
#         session.add(user_2)
#         session.commit()

# create_users()

@router.get("/api/users", status_code=200)
async def get_users():
    # return read_users()
    with Session(engine) as session:
        # statement = select(User)
        statement = select(User).limit(3)
        results = session.exec(statement)
        users = results.all()
        return users

@router.get("/api/users/by-id/{id}", status_code=200)
async def get_user_by_id(*, id: int):
    with Session(engine) as session:
        # statement = select(User).where(User.id == id)
        # result = session.exec(statement)
        # user = result.all()
        # return user
        return session.get(User, id)
    
# @router.get("/api/users/by-username/{username}", status_code=200)
# async def get_user_by_username(*, username: str):
#     with Session(engine) as session:
#         statement = select(User).where(User.username == username)
#         result = session.exec(statement)
#         user = result.all()
#         return user

@router.get("/api/users/by-username/{username}", status_code=200)
async def get_user_by_username(*, username: str):
    with Session(engine) as session:
        statement = select(User).where(User.username == username)
        result = session.exec(statement)
        user = result.all()
        return user

@router.put("/api/users/{id}", status_code=201)
# async def update_user(*, session: Session = Depends(get_session), id: int, user: User):
async def update_user(*, session: Session = Depends(get_session), id: int, user: UserUpdate):
    db_user = session.get(User, id)
    # user_update = session.get(User, id)
    # user_update.username = user.username
    # user_update.password = user.password
    # user_update.age = user.age
    # session.add(user_update)
    # session.commit()
    user_data = user.model_dump(exclude_unset=True)
    for k, v in user_data.items():
        setattr(db_user, k, v)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
