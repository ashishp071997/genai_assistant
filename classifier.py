# classifier.py

def classify_question(question):
    question = question.lower()

    if "spend" in question or "total" in question:
        return "SQL"
    if "policy" in question or "refund" in question:
        return "RAG"
    return "BOTH"
