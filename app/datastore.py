import psycopg2
import torch
from llama_index.core import PromptTemplate, Settings, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.vector_stores.postgres import PGVectorStore
from sqlalchemy import make_url
from transformers import BitsAndBytesConfig

from .config import CONNECTION_STRING, DB_NAME, HF_TOKEN, TABLE_NAME

db_connection = psycopg2.connect(CONNECTION_STRING)
db_connection.autocommit = True


quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
)

llama = HuggingFaceLLM(
    model_name="meta-llama/Llama-2-7b-chat-hf",
    tokenizer_name="meta-llama/Llama-2-7b-chat-hf",
    query_wrapper_prompt=PromptTemplate("<s> [INST] {query_str} [/INST] </s>"),
    context_window=3900,
    model_kwargs={"token": HF_TOKEN, "quantization_config": quantization_config},
    tokenizer_kwargs={"token": HF_TOKEN},
    device_map="cuda",
)

Settings.llm = llama
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

url = make_url(CONNECTION_STRING)


vector_store = PGVectorStore.from_params(
    database=DB_NAME,
    host=url.host,
    password=url.password,
    port=url.port,
    user=url.username,
    table_name=TABLE_NAME,
    embed_dim=384,
    hybrid_search=True,
    text_search_config="french",
)

storage_context = StorageContext.from_defaults(vector_store=vector_store)
