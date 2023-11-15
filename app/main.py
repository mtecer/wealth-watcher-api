# import json
import uvicorn

from fastapi import FastAPI
# from pathlib import Path
from pprint import pprint

from fastapi.staticfiles import StaticFiles

from app.api import users, ping
from app.views import index
from app.database import create_db_and_tables, load_mock_data

api = FastAPI()

def configure_routing():
    api.mount("/static", StaticFiles(directory="app/static"), name="static")
    api.include_router(ping.router)
    api.include_router(index.router)
    api.include_router(users.router)

def configure_db():
    create_db_and_tables()
    # load_mock_data()

def main():
    configure_routing()
    configure_db()
    
if __name__ == "__main__":
    main()
    # users = read_users()
    uvicorn.run(api, host="127.0.0.1", port=8081, reload=True)
else:
    main()
    # users = read_users()
