from rag.retriever import retrieve

print(retrieve("What is the refund policy?", top_k=2))
