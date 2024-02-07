import subprocess
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config import settings


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    TO FILL IN
    """

    try:
        subprocess.run(
            [
                "tailwindcss",
                "-i",
                str(settings.STATIC_DIR / "src" / "tw.css"),
                "-o",
                str(settings.STATIC_DIR / "css" / "main.css"),
            ]
        )
    except Exception as e:
        raise RuntimeError from e
    yield
