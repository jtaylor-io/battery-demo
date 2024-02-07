import random

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
    # TODO: add to db entity
    featured_products = [
        {"name": "Duracell AA", "src_path": "../static/images/battery-duracell-aa.jpg"},
        {"name": "Linux AA", "src_path": "../static/images/battery-linux-aa.jpg"},
        {"name": "GP CR2032", "src_path": "../static/images/battery-gp-cr2032.jpg"},
    ]
    context = {
        "request": request,
        "featured_product": random.choice(featured_products),
    }
    if request.headers.get("HX-Request"):
        block_name = "featured_product"
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
