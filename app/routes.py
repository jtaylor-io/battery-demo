from fastapi import APIRouter, Request
from jinja2_fragments.fastapi import Jinja2Blocks

from app.config import Settings

settings = Settings()
router = APIRouter()
templates = Jinja2Blocks(settings.TEMPLATE_DIR)


@router.get("/")
def home(request: Request):
    template = "home.html"
    block_name = None
    context = {"request": request}
    if request.headers.get("HX-Request"):
        block_name = "content"
    return templates.TemplateResponse(template, context, block_name=block_name)


@router.get("/about")
def about(request: Request):
    template = "about.html"
    block_name = None
    context = {"request": request}
    if request.headers.get("HX-Request"):
        block_name = "content"
    return templates.TemplateResponse(template, context, block_name=block_name)


@router.get("/products")
def products(request: Request):
    template = "products.html"
    block_name = None
    context = {"request": request}
    if request.headers.get("HX-Request"):
        block_name = "content"
    return templates.TemplateResponse(template, context, block_name=block_name)


@router.get("/detail")
def detail(request: Request):
    template = "detail.html"
    block_name = None
    context = {"request": request}
    if request.headers.get("HX-Request"):
        block_name = "content"
    return templates.TemplateResponse(template, context, block_name=block_name)
