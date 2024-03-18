import datetime
import logging

import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

# from app.embeddings import create_embeddings
# from app.query_engine import model_pipeline
from app.data_model import LmResponse, UserQuery

app = FastAPI()
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.StreamHandler())


ALLOWED_ORIGINS = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_body_logger(request: Request, call_next):
    print(await request.body())
    response = await call_next(request)
    return response


@app.get("/")
def healthcheck():
    return {"message": "Hello World!"}


@app.post("/query")
def query_index(data: UserQuery):
    return {"response": "Hello from Llama 2", "input": data}
