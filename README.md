# RAG using Cosine Similarity + Ollama

A minimal Retrieval-Augmented Generation (RAG) pipeline using:
- Bag-of-words cosine similarity
- Local LLM inference via Ollama

## How it works
1. User query is compared against a document corpus
2. Most relevant document is selected
3. The document is injected into an LLM prompt
4. Ollama generates a short recommendation

## Requirements
- Python 3.9+
- Ollama running locally
- Model pulled (example: gemma3:1b)

## Run
```bash
pip install -r requirements.txt
python src/rag.py

Notes

This project is for learning and demonstration purposes.


---

## How to move your current file correctly

From Terminal:

```bash
mkdir -p rag-ollama/src
mv ~/Downloads/rag.py rag-ollama/src/
cd rag-ollama

Test before pushing:

python src/rag.py