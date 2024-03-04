import os
from typing import Final, Optional

HF_TOKEN: Optional[str] = os.getenv("HF_TOKEN")
CONNECTION_STRING: Final[str] = os.getenv("DB_URL")
DATASET_URL = os.getenv("DATA_URL")
DB_NAME: Final[str] = "example"
TABLE_NAME: Final[str] = "custom_embeddings"
DATA_DIR = "../data"
