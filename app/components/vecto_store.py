from langchain_community.vectorstores import FAISS
from app.components.embeddings import get_embedding_model
from app.utilities.logger import get_logger
from app.utilities.custom_exception import CustomException
from app.config.config import DB_FIASS_PATH
import os

logger = get_logger(__name__)

def load_vectore_store():
    try:
        embedding_model = get_embedding_model()
        if os.path.exists(DB_FIASS_PATH):
            logger.info("loading existing Vectorestore")
            return FAISS.load_local(
                DB_FIASS_PATH,
                embedding_model,
                allow_dangerous_deserialization=True
            )
        else:
            logger.warning("No Vectorstore Found")
    except Exception as e:
        error_message = CustomException("Failed to load vectorstore", e)
        logger.error(str(error_message))

def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No chunks were found")
        
        logger.info("generating your new vectorstore")

        embedding_model = get_embedding_model()

        db = FAISS.from_documents(text_chunks, embedding_model)

        logger.info("saving vector store")

        db.save_local(DB_FIASS_PATH)

        logger.info("Vector save successfully")

        return db
    except Exception as e:
        error_message = CustomException("Failed to create new vectorstore", e)
        logger.error(str(error_message))