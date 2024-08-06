from fastapi import FastAPI

from routers.api_v1 import api_v1_router

app = FastAPI()

app.include_router(api_v1_router, prefix="/api/v1")
