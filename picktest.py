import pickle

docs = pickle.load(open("genai_assistant/rag/policies.pkl", "rb"))

print("TOTAL DOCS:", len(docs))
print("FIRST DOC:\n", docs[0::])
