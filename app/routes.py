import random
import re
from typing import Annotated

from fastapi import APIRouter, Form, Request
from jinja2_fragments.fastapi import Jinja2Blocks
from tinydb import Query, TinyDB, where

from app.config import Settings

settings = Settings()
router = APIRouter()
templates = Jinja2Blocks(settings.TEMPLATE_DIR)

# TODO: this is obviously NOT a solid persistence choice for scale, consitency,...!
db = TinyDB(
    settings.DATA_DIR / "db.json", sort_keys=True, indent=4, separators=(",", ": ")
)


@router.get("/")
def home(request: Request):
    template = "home.html"
    block_name = None
    # TODO: have some way of selecting which items are featured
    featured_product = random.choice(db.all())
    context = {
        "request": request,
        "featured_product": featured_product,
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
    products = db.all()
    template = "products.html"
    block_name = None
    context = {"request": request, "products": products}

    if request.headers.get("HX-Request"):
        template = "product/summary.html"

        if "toggle" not in request.headers.get("HX-Trigger"):
            id = request.headers.get("HX-Trigger")
            context["product"] = db.get(where("id") == id)
            block_name = "product_summary"
        else:
            id = request.headers.get("product-id")
            context["product"] = db.get(where("id") == id)
            block_name = "product_name"

    return templates.TemplateResponse(template, context, block_name=block_name)


@router.get("/search")
def search_get(request: Request):
    products = db.all()

    context = {
        "request": request,
        "products": products,
        "from_search": True,
    }
    block_name = None

    if request.headers.get("HX-Request"):
        block_name = "content"

    return templates.TemplateResponse("products.html", context, block_name=block_name)


@router.post("/search")
def search_post(request: Request, search: Annotated[str, Form()]):
    print("search", search)
    Product = Query()
    products = db.search(Product.name.search(search, re.IGNORECASE))

    context = {
        "request": request,
        "products": products,
        "from_search": True,
    }
    block_name = None
    if request.headers.get("hx-request"):
        block_name = "product_cards"

    return templates.TemplateResponse("products.html", context, block_name=block_name)


@router.get("/detail")
def artist_details(request: Request, doc_id: int | None = None):
    template = "product/details.html"
    block_name = None
    if not request.headers.get("HX-Request"):
        doc_id = 1
    else:
        block_name = "details"

    product = db.get(doc_id=doc_id)
    next_id = doc_id + 1

    context = {
        "request": request,
        "product": product,
        "next_id": next_id,
    }
    return templates.TemplateResponse(template, context, block_name=block_name)
