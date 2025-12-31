from .db import init_db, get_customer_spend
from .rag.retriever import retrieve
from .classifier import classify_question
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException

app = FastAPI(title="GenAI Assistant")


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
    try:
        question = req.question
        mode = classify_question(question)
        context = ""

        # Create DB connection per request (SAFE)
        con = init_db()

        if mode in ["SQL", "BOTH"]:
            if "john" in question.lower():
                result = get_customer_spend(con, "John")
                context += f"John total spend: {result[1]}\n"
            else:
                context += "No customer identified for SQL query.\n"

        if mode in ["RAG", "BOTH"]:
            docs = retrieve(question)
            context += "Policy Info:\n" + "\n".join(docs)

        return {
            "question": question,
            "mode": mode,
            "answer": f"Answer based on verified data:\n{context}"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


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