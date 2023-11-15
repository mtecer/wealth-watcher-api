# from pathlib import Path

from sqlmodel import Field, Session, SQLModel, create_engine, select, or_, col

from app.config import sqlite_url
from app.models import User

engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def load_mock_data():
    user_1 = User(username="user_1", password="password123")
    user_2 = User(username="user_2", password="password456", age=21)
    user_3 = User(username="user_3", password="password789", age=38)
    user_4 = User(username="user_4", password="password012", age=57)

    with Session(engine) as session:
        session.add(user_1)
        session.add(user_2)
        session.add(user_3)
        session.add(user_4)
        session.commit()