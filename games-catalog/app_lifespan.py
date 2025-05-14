from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from api.build_jsonapi_app import add_routes
from core.models import db_helper as db


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    builder = add_routes(app)
    builder.initialize()
    yield
    await db.engine.dispose()
