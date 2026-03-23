from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/about", tags=["About"])
templates = Jinja2Templates(directory="templates")

@router.get("/")
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})