from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

app = FastAPI()

class Query(BaseModel):
    question: str

# Load the vectorstore
embedding = OpenAIEmbeddings()
db = FAISS.load_local("faiss_index", embedding)
retriever = db.as_retriever()

# Create RAG chain
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo"),
    retriever=retriever,
    return_source_documents=True
)

@app.post("/ask")
async def ask_question(query: Query):
    result = qa_chain({"query": query.question})
    return {
        "question": query.question,
        "answer": result["result"],
        "sources": [doc.metadata for doc in result["source_documents"]]
    }
