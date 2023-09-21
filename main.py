import json
import uvicorn

from fastapi import FastAPI
from pathlib import Path
from pprint import pprint

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
    
    # base_dir = Path(__file__).resolve().parent
    # data_dir = Path(module_dir / "data")
    # file_path = Path(data_dir / "users.json")
    # file2_path = Path(data_dir / "users-2.json")
    
    # users_datafile = Path(base_dir / "data" / "users.json")
    # users = json.loads(users_datafile.read_text())

    # print(type(users))
    # users.append({
    #     "id": "e77acc31-223b-46e7-9664-dea41e8b091c",
    #     "user_name": "user_4",
    #     "name": "User Four"
    # })
    # users_datafile.write_text(json.dumps(users, indent=4))

    # pprint(users, indent=4)
    # content = file_path.read_text()
    # content_dict = json.loads(content)

    # pprint(content_dict, indent=4)
    # content_dict.append({
    #     "id": "e77acc31-223b-46e7-9664-dea41e8b091c",
    #     "user_name": "user_4",
    #     "name": "User Four"
    # })
    # print(type(content_dict))
    # print(content_dict)
    # file2_path.write_text(json.dumps(content_dict, indent=4))

    # print(module_dir)
    # print(data_dir)

    # print(Path.cwd())
    # print(Path(__file__))
    # print(Path(__file__).resolve())
    # print(Path(__file__).resolve().stem)
    # print(Path(__file__).stem) # main
    # print(Path(__file__).name) # main.py
    # print(Path(__file__).basename)
    # print(Path(__file__).resolve().parent) # /Users/mtecer/Projects/wealth-watcher-api
    # print(Path(__file__).resolve().parent.parent) # /Users/mtecer/Projects

if __name__ == "__main__":
    configure()
    # users = read_users()
    uvicorn.run(api, host="127.0.0.1", port=8081)
else:
    configure()
    # users = read_users()
