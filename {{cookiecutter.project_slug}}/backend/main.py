from asyncio.log import logger

from app.core.factory import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting")

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=int("{{ cookiecutter.backend_port }}"),
    )
