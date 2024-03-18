import datetime

import uvicorn
from fastapi import FastAPI

# from app.embeddings import create_embeddings
# from app.query_engine import model_pipeline
from app.data_model import LmResponse, UserQuery

app = FastAPI()


@app.get("/")
def healthcheck():
    return {"message": "Hello World!"}


@app.post("/query")
def query_index(data: UserQuery) -> LmResponse:

    return LmResponse(
        message="Hello from Llama 2",
        sent_at=datetime.datetime.now(),
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8300)
