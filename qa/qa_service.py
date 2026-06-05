# ==========================================
# File: qa/qa_service.py
# ==========================================


from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from core.logger import get_logger

logger = get_logger(__name__)

class QAService:
    def __init__(self,api_key,model="openai/gpt-oss-20b"):
        self.llm = ChatGroq(api_key=api_key, model=model)

    def ask(self,question,documents):
        context = "\n\n".join([doc.page_content for doc in documents])

        prompt = f"""
                You are a document intelligence assistant.
                Answer ONLY using the provided context.
                If the answer is not present in the context, say:
                "I could not find that information in the document."
                Context:
                {context}
                Question:
                {question}
                """

        response = self.llm.invoke([HumanMessage(content=prompt)])
        return response.content
