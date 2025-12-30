# rag/retriever.py
from sentence_transformers import SentenceTransformer
import faiss, pickle



index = faiss.read_index("genai_assistant/rag/policies.index")
docs = pickle.load(open("genai_assistant/rag/policies.pkl", "rb"))

def retrieve(query, top_k=2):
    
    model = SentenceTransformer("all-MiniLM-L6-v2")
    q_emb = model.encode([query])
    _, idx = index.search(q_emb, top_k)
    return [docs[i] for i in idx[0]]
