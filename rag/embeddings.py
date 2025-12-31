# rag/embeddings.py
from sentence_transformers import SentenceTransformer
import faiss, pickle, os



def build_index():
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # read policies.txt
    os.makedirs("rag", exist_ok=True)
    with open("genai_assistant/data/policies.txt", "r") as f:
        content = f.read()
        docs = content.strip().split("\n\n")
       

    embeddings = model.encode(docs)

    # create FAISS index
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(embeddings)

    # save index and docs
    faiss.write_index(index, "genai_assistant/rag/policies.index")
    pickle.dump(docs, open("genai_assistant/rag/policies.pkl", "wb"))

if __name__ == "__main__":
    build_index()
