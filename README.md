
Below is a **complete, professional README.md** you can directly copy-paste into your project.
This is **resume-ready + GitHub-ready + interview-ready**.

---

# 🧠 GenAI Assistant with DuckDB + RAG (FAISS)

An **end-to-end GenAI project** that combines **structured analytics (DuckDB)** and **unstructured knowledge retrieval (RAG using FAISS)**, exposed via a clean Python architecture.

This project demonstrates **how real-world GenAI systems are built** — not just prompts.

---

## 🚀 Features

* ✅ **DuckDB** for fast, embedded analytics on CSV data
* ✅ **RAG (Retrieval-Augmented Generation)** using:

  * Sentence Transformers
  * FAISS vector search
* ✅ **Hybrid intelligence**

  * SQL for structured questions
  * RAG for policy / document questions
* ✅ **Production-ready patterns**

  * Persistent database
  * Precomputed embeddings
  * Clean separation of concerns

---

## 🏗️ Architecture Overview

```
User Question
     │
     ▼
Classifier
(SQL / RAG / BOTH)
     │
     ├── SQL → DuckDB (analytics.db)
     │
     └── RAG → FAISS (policies.index + policies.pkl)
                     │
                     ▼
               Relevant Context
                     │
                     ▼
                Final Answer
```

---

## 📁 Project Structure

```
genai_assistant/
│
├── data/
│   ├── customers.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── products.csv
│   └── policies.txt
│
├── rag/
│   ├── embeddings.py      # Build FAISS index
│   ├── retriever.py       # Query FAISS index
│   ├── policies.index     # Vector index (auto-generated)
│   └── policies.pkl       # Original documents
│
├── db.py                  # DuckDB logic
├── classifier.py          # Question routing
├── test_retriever.py      # RAG test script
├── analytics.db           # Persistent DuckDB file
└── requirements.txt
```

---

## 🧠 Core Concepts Explained

### 🔹 DuckDB (Structured Data)

* Embedded analytical database
* Reads CSV files directly
* Supports complex joins & aggregations
* Stored as a **persistent file (`analytics.db`)**

Used for:

* Customer spend
* Order analytics
* Revenue calculations

---

### 🔹 RAG (Unstructured Data)

#### Files:

* **`policies.index`**

  * FAISS vector index
  * Stores numerical embeddings
* **`policies.pkl`**

  * Original policy text
  * Maps FAISS search results → readable text

#### Why both?

FAISS returns **indices, not text**.
The `.pkl` file translates indices back to documents.

---

## ⚙️ Setup Instructions

### 1️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Build embeddings (IMPORTANT)

Run once (or when `policies.txt` changes):

```bash
cd genai_assistant
python rag/embeddings.py
```

This creates:

```
rag/policies.index
rag/policies.pkl
```

---

### 4️⃣ Test RAG retrieval

```bash
python test_retriever.py
```

Expected output:

```
Refunds are allowed within 30 days...
```

---

## 🧪 Example Usage

### RAG Query

```python
from rag.retriever import retrieve

retrieve("What is the refund policy?")
```

### SQL Analytics

```python
from db import init_db, get_customer_spend

con = init_db()
get_customer_spend(con, "John")
```

---

## 🛡️ Best Practices Used

* SQL parameter binding (prevents injection)
* Precomputed embeddings (fast inference)
* Separation of indexing vs retrieval
* Ignoring `__pycache__` via `.gitignore`

---

## 🧠 Interview Talking Points ⭐

* “I used DuckDB for embedded analytics instead of a heavy OLAP engine.”
* “RAG is implemented using FAISS where vectors and original documents are stored separately.”
* “The system supports hybrid reasoning: SQL + semantic search.”
* “Embeddings are precomputed to reduce runtime latency.”

---

## 🚀 Possible Extensions

* 🔐 Authentication & rate limiting
* 📊 Streamlit / FastAPI UI
* 🔍 Hybrid search (keyword + vector)
* 🧠 LLM integration (OpenAI / Ollama / HuggingFace)
* ☁️ Docker + Cloud deployment

---

## 👤 Author

**Ashish Prajapati**
Data Engineer / GenAI Enthusiast

