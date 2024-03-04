import logging

from datasets import load_dataset
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

from .config import DATA_DIR, DATASET_URL, DB_NAME, HF_TOKEN
from .datastore import db_connection

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())


def create_embeddings():
    data = load_dataset(DATASET_URL, token=HF_TOKEN)
    data["train"].to_json(DATA_DIR)
    documents = SimpleDirectoryReader(DATA_DIR).load_data(show_progress=True)

    logger.info(f"Recreating the database: {DB_NAME}")

    try:
        with db_connection.cursor() as cursor:
            cursor.execute(f"DROP DATABASE IF EXISTS {DB_NAME}")
            cursor.execute(f"CREATE DATABASE {DB_NAME}")

        logger.info(f"{DB_NAME} created successfully")
    except Exception as e:
        logger.error(f"Failed to create {DB_NAME}.\nError:\n{e}")

    index = VectorStoreIndex.from_documents(documents, show_progress=True)
