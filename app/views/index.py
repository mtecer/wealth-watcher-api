from fastapi import APIRouter, Request

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {
        "request": request,
        # "css_relative_path": "static/css/style.css",
        "api_name": "Wealth Watcher API",
    }
    # return templates.TemplateResponse("index.html", {"request": request})
    return templates.TemplateResponse("index.html", context)
