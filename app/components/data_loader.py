import os
from app.components.PDF_loader import load_PDF_files, create_text_chunks
from app.components.vecto_store import save_vector_store
from app.config.config import DB_FIASS_PATH

from app.utilities.logger import get_logger
from app.utilities.custom_exception import CustomException

logger = get_logger(__name__)

def process_store_pdfs():
    try:
        logger.info("making the vectorstore")
        documents = load_PDF_files()
        text_chunks = create_text_chunks(documents)
        save_vector_store(text_chunks)

    except Exception as e:
        error_message = CustomException("failed to create vector store")
        logger.error(str(error_message))

if __name__ == "__main__":
    process_store_pdfs()



