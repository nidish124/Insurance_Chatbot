from langchain.chat_models import init_chat_model
#from app.config.config import OPENAI_MODEL
from app.utilities.logger import get_logger
from app.utilities.custom_exception import CustomException
import os


logger = get_logger(__name__)

def load_llm(openai_model = "openai:gpt-4"):
    try:
        logger.info("loading LLM from Huggingface")
        api_key = os.environ.get("OPENAI_API_KEY")
        llm = init_chat_model(model = openai_model,
                              api_key = api_key,
                              model_kwargs={
                                "temperature": 0.3
    })
        if not llm:
            raise CustomException("LLM Not Loaded")
        logger.info("LLM loaded successfully")

        return llm
    
    except Exception as e:
        error_message = CustomException("Failed to load LLM", e)
        logger.error(str(error_message))

