from langchain_core.prompts import PromptTemplate

from app.components.llm import load_llm
from app.components.vecto_store import load_vectore_store

#from app.config.config import OPENAI_MODEL
from app.utilities.logger import get_logger
from app.utilities.custom_exception import CustomException
from langchain.tools import tool
from langchain.agents import create_agent

logger = get_logger(__name__)

CUSTOM_PROMPT_TEMPLATE = """ Answer the following insurance question in 2-3 lines maximum using only the information provided in the Tools provided.

Answer: 
"""

@tool(response_format="content_and_artifact")
def retrieve_context(vector_store, query: str):
    """Retrieve information to help answer a query."""
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    retrieved_docs = retriever.invoke(query)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

def create_qa_chain():
    try:
        logger.info("Loading vectorstore for context")

        db = load_vectore_store()

        if db is None:
            raise CustomException("vector store not present or empty")
        
        llm = load_llm("openai:gpt-4")

        if llm is None:
            raise CustomException("LLM not loaded in retriever")
        
        tools = [retrieve_context]

        agent = create_agent(llm, tools, system_prompt=CUSTOM_PROMPT_TEMPLATE)

        if not agent:
            raise CustomException("Agent is not created successfully")

        logger.info("successfully created QA Chain")
        return agent
    
    except Exception as e:
        error_message = CustomException("Failed to make a QA chain", e)
        logger.error(str(error_message))
