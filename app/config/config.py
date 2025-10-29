import os
OPENAI_API_KEY= os.environ.get("OPENAI_API_KEY")
DB_FIASS_PATH= "Vectorstore/db_faiss"
OPENAI_MODEL= "openai:gpt-4"
DATA_PATH= "data/"
CHUNK_SIZE= 500
CHUNK_OVERLAP= 50
