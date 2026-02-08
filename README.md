# RAG from Scratch (Cosine Similarity + Ollama)

A minimal **Retrieval-Augmented Generation (RAG)** implementation built **from scratch** using pure Python and a locally running LLM via Ollama.

No embeddings.  
No vector databases.  
No RAG frameworks.

---

## How It Works

User Query
→ Bag-of-Words
→ Cosine Similarity
→ Top Document Retrieval
→ Prompt Augmentation
→ Local LLM (Ollama)


---

## Key Features

- Manual document retrieval using bag-of-words
- Cosine similarity implemented from first principles
- Context injection into LLM prompts
- Local inference via Ollama API

---

## Project Structure

```text
rag-ollama/
├── src/
│   └── rag.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
Requirements
Python 3.9+

Ollama running locally

Model pulled (example)

ollama pull gemma3:1b
Run
pip install -r requirements.txt
python src/rag.py
Notes
This project is intentionally simple to expose core RAG mechanics before introducing embeddings or vector databases.

License
MIT


