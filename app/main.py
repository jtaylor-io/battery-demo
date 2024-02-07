from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.config import Settings
from app.helpers import lifespan
from app.routes import router

settings = Settings()


def get_app() -> FastAPI:
    """TO FIll IN"""

    app = FastAPI(lifespan=lifespan, **settings.fastapi_kwargs)
    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")
    app.include_router(router)

    return app


app = get_app()
