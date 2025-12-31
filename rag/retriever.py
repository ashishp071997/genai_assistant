# rag/retriever.py
from sentence_transformers import SentenceTransformer
import faiss, pickle



index = faiss.read_index("genai_assistant/rag/policies.index")
docs = pickle.load(open("genai_assistant/rag/policies.pkl", "rb"))

def retrieve(query, top_k=3, threshold=1.2):
    
    model = SentenceTransformer("all-MiniLM-L6-v2")
    q_emb = model.encode([query])
    scores, idx = index.search(q_emb, top_k)

    result =[]

    for score , i in zip(scores[0],idx[0]):
        if score<threshold:
            result.append(docs[i])
    if not result:
        return 'No relevant policy found'
    
    return result
    #return [docs[i] for i in idx[0]]
