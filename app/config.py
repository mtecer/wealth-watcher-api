import json

from pathlib import Path

base_dir = Path(__file__).resolve().parent    
users_datafile = Path(base_dir / "data" / "users.json")

def read_users():
    users = json.loads(users_datafile.read_text())
    return users

def write_users(users: list[dict]):
    users_datafile.write_text(json.dumps(users, indent=4))
