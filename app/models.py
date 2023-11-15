# from sqlmodel import SQLModel, Field

# class User(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     uid: 
#     username: str = Field(default=None, index=True)
#     password: str

from sqlmodel import SQLModel, Field

from uuid import uuid4

def generate_uuid4() -> str:
    return str(uuid4())

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    uid: str = Field(default_factory=generate_uuid4)
    username: str = Field(default=None, index=True)
    password: str
    age: int | None = Field(default=None, index=True)

class UserUpdate(SQLModel):
    username: str | None = None
    password: str | None = None
    age: int | None = None
