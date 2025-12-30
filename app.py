# app.py
from .db import init_db, get_customer_spend
from .rag.retriever import retrieve
from .classifier import classify_question
from pydantic import BaseModel
import duckdb
from fastapi import FastAPI

#Adding for production 
app = FastAPI(title="Genai Assistant")

# Initialize DB once (IMPORTANT)
con =init_db()


# ----------------------
# Request schema
# ----------------------
class QueryRequest(BaseModel):
    question: str


# ----------------------
# Health check
# ----------------------
@app.get("/")
def health():
    return {"status": "running"}


# ----------------------
# Main GenAI endpoint
# ----------------------
@app.post("/query")
def query(req: QueryRequest):
    question = req.question
    mode = classify_question(question)

    context = ""

    if mode in ["SQL", "BOTH"]:
        if "john" in question.lower():
            result = get_customer_spend(con, "John")
            context += f"John total spend: {result[1]}\n"

    if mode in ["RAG", "BOTH"]:
        docs = retrieve(question)
        context += "Policy Info:\n" + "".join(docs)

    return{ 
        "question": question,
        "mode": mode,
        "answer": f"Answer based on verified data:\n{context}"
    }


#CLI Code 

'''
# app.py
from db import init_db, get_customer_spend
from rag.retriever import retrieve
from classifier import classify_question
import duckdb
from fastapi import FastAPI

#app = FastAPI(title="Genai Assistant")


def generate_answer(question):
    con =init_db()
    
    mode = classify_question(question)

    context = ""

    if mode in ["SQL", "BOTH"]:
        if "john" in question.lower():
            result = get_customer_spend(con, "John")
            context += f"John total spend: {result[1]}\n"

    if mode in ["RAG", "BOTH"]:
        docs = retrieve(question)
        context += "Policy Info:\n" + "".join(docs)

    return f"""
Answer based on verified data: {context}
"""

if __name__ == "__main__":
    q = input("Ask a question: ")
    print(generate_answer(q))


'''