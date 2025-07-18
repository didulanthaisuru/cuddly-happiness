from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hii")
def read_root():
    print("halo world")
    return {"message": "halo world"}
