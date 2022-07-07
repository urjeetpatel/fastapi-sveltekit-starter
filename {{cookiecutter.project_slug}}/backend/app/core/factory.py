from fastapi import FastAPI

from app.core.config import settings
from app.core.models import HealthCheck


def create_app():
    app = FastAPI(
        title=settings.PROJECT_NAME, version=settings.VERSION, debug=settings.DEBUG
    )
    setup_routers(app=app)
    return app


def setup_routers(app: FastAPI) -> None:
    @app.get("/", response_model=HealthCheck, tags=["status"])
    async def healthcheck():
        return {
            "name": settings.PROJECT_NAME,
            "version": settings.VERSION,
            "description": "",
        }
