from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_items():
    return {"message": "List of items"}

@router.get("/{item_id}")
async def read_item(item_id: int):
    return {"message": f"Item {item_id}"}
