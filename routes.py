from fastapi import APIRouter

# Router object create kar rahe hain
router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello World from routes file!"}

@router.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "status": "Success"}