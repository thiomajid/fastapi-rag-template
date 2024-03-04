import logging

from llama_index.core import VectorStoreIndex
from transformers import MarianMTModel, MarianTokenizer

from .datastore import vector_store

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

translation_model_name = "Helsinki-NLP/opus-mt-en-fr"
tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
translation_model = MarianMTModel.from_pretrained(translation_model_name)


index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
query_engine = index.as_query_engine(response_mode="compact")


def translate(text: str) -> str:
    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = translation_model.generate(
        inputs,
        num_beams=4,
        max_length=500,
        early_stopping=True,
    )
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translated_text


def model_pipeline(message: str):
    response = query_engine.query(message).response
    translated_response = translate(response)

    return translated_response
