import uvicorn

from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles

api = FastAPI()

from api import users
from views import index

def configure_routing():
    api.mount("/static", StaticFiles(directory="static"), name="static")
    api.include_router(index.router)
    api.include_router(users.router)

def configure():
    configure_routing()

if __name__ == "__main__":
    configure()
    uvicorn(api, host="127.0.0.1", port=8081)
else:
    configure()
