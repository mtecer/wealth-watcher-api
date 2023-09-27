import json
import uvicorn

from fastapi import FastAPI
from pathlib import Path
from pprint import pprint

from fastapi.staticfiles import StaticFiles

api = FastAPI()

from api import users, ping
from views import index

def configure_routing():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(ping.router)
    api.include_router(index.router)
    api.include_router(users.router)

def configure():
    configure_routing()
    
if __name__ == "__main__":
    configure()
    # users = read_users()
    uvicorn.run(api, host="127.0.0.1", port=8081, reload=True)
else:
    configure()
    # users = read_users()
