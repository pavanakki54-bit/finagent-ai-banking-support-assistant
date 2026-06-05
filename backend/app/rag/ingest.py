from app.rag.retriever import load_documents

def ingest_documents() -> dict:
    docs = load_documents()
    return {"status": "indexed", "chunks": len(docs)}
