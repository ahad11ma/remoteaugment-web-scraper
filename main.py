from fastapi import FastAPI
import uvicorn

app = FastAPI(title="My Single-File App")

@app.get("/")
def read_root():
    return {"message": "Hello World from one main file!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "status": "Success"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)