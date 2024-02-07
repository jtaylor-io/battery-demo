from pathlib import Path
from typing import Any

from fastapi.responses import HTMLResponse
from pydantic_settings import BaseSettings

APP_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    APP_DIR: Path = APP_DIR

    STATIC_DIR: Path = APP_DIR / "static"
    TEMPLATE_DIR: Path = APP_DIR / "templates"
    DATA_DIR: Path = APP_DIR.parent / "data"

    FASTAPI_PROPERTIES: dict = {
        "title": "Amp it Up!",
        "description": "Demo site to showcase HTMX as a lightweight frontend alternative.",
        "version": "0.0.1",
        "default_response_class": HTMLResponse,  # HTMX expects HTML fragments
    }

    DISABLE_DOCS: bool = True

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        """TO FILL IN"""
        fastapi_kwargs = self.FASTAPI_PROPERTIES
        if self.DISABLE_DOCS:
            fastapi_kwargs.update(
                {
                    "openapi_url": None,
                    "openapi_prefix": None,
                    "docs_url": None,
                    "redoc_url": None,
                }
            )
        return fastapi_kwargs


settings = Settings()
