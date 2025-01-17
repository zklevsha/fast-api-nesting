from fastapi import APIRouter, FastAPI

from .items import router as items_router
from .users import router as users_router

api_v1_router = APIRouter()


@api_v1_router.get("/hello")
async def hello():
    return {"message": "API v1"}

@api_v1_router.get("/goodbye")
async def goodbye():
    return {"message": "Goodbye"}

api_v1_router.include_router(items_router, prefix="/items", tags=["items"])
api_v1_router.include_router(users_router, prefix="/users", tags=["users"])
