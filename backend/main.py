from fastapi import FastAPI

from app.config.settings import settings

from app.core.logger import logger


app = FastAPI(

    title=settings.PROJECT_NAME,

    version=settings.VERSION,

    description="AI Powered Insider Threat Detection Platform"

)

@app.get("/")

async def home():

    logger.info("Home Endpoint Accessed")

    return {

        "project": settings.PROJECT_NAME,

        "version": settings.VERSION,

        "status": "running"

    }

from app.api.health import router as health_router

app.include_router(health_router)