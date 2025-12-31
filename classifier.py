# classifier.py

def classify_question(question):
    question = question.lower()

    sql_keywords = ["spend", "total", "amount", "purchase"]
    rag_keywords = ["policy", "leave", "shipping", "refund", "cancellation"]

    is_sql = any(k in question for k in sql_keywords)
    is_rag = any(k in question for k in rag_keywords)
    
    if is_sql and is_rag:
        return "BOTH"
    elif is_sql:
        return "SQL"
    elif is_rag:
        return "RAG"
    else:
        return "UNKNOWN"
'''
    if "spend" in question or "total" in question:
        return "SQL"
    if "policy" in question or "refund" in question:
        return "RAG"
    return "BOTH"'''
