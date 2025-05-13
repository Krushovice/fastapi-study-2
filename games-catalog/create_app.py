from fastapi import FastAPI
from fastapi.responses import ORJSONResponse as JSONResponse

from app_lifespan import lifespan


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI and SQLAlchemy",
        lifespan=lifespan,
        debug=True,
        default_response_class=JSONResponse,
        docs_url="/docs",
        openapi_url="/openapi.json",
    )
    return app
