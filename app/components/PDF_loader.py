import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.utilities.logger import get_logger
from app.utilities.custom_exception import CustomException
from app.config.config import DATA_PATH, CHUNK_SIZE, CHUNK_OVERLAP

logger = get_logger(__name__)

def load_PDF_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException("Data path does not exists")
        
        logger.info(f"Loading files from {DATA_PATH}")

        loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls = PyPDFLoader)

        documents = loader.load()

        if not documents:
            logger.warning("No pdf's were found")
        else:
            logger.info(f"successfully fetched {len(documents)} documents")

        return documents

    except Exception as e:
        logger.error("Error in PDF Loader module")
        raise CustomException("error in PDF Loader", e)
        

def create_text_chunks(documents):
    try:
        if not documents:
            raise CustomException("No documents")
        
        logger.info(f"Splitting {len(documents)} documents into chunks")

        text_splitter = RecursiveCharacterTextSplitter(chunk_size = CHUNK_SIZE, chunk_overlap = CHUNK_OVERLAP)

        text_chunk = text_splitter.split_documents(documents)

        logger.info(f"generated {len(text_chunk)} text chunks")

        return text_chunk

    except Exception as e:
        error_message = CustomException("error in PDF Loader", e)
        logger.error(str(error_message))