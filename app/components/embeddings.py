from langchain_openai import OpenAIEmbeddings
from app.utilities.logger import get_logger
from app.utilities.custom_exception import CustomException
import os

logger = get_logger(__name__)

def get_embedding_model():
    try:
        logger.info("installing our Huggingface embedding model")
        api_key = os.environ.get("OPENAI_API_KEY")
        model  =  OpenAIEmbeddings(api_key=api_key,
            model="text-embedding-ada-002")

        logger.info("embedding model loaded")

        return model
    except Exception as e:
        error_message = CustomException("error in loading embedding model", e)
        logger.error(str(error_message))