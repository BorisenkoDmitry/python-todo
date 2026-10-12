from fastapi import FastAPI

from taskflow_api.api.routes.health import router as health_router

app = FastAPI(title="TaskFlow API", version="0.1.0")

app.include_router(health_router)