from pathlib import Path
from typing import List, Dict

DATA_DIR = Path(__file__).resolve().parents[3] / "data"

KEYWORDS = {
    "payment": ["payment", "ach", "transfer", "pending", "delay"],
    "account": ["account", "balance", "profile", "checking", "savings"],
    "eligibility": ["eligibility", "eligible", "qualify", "loan", "credit"],
    "support": ["escalate", "human", "ticket", "support", "agent"]
}

def load_documents() -> List[Dict[str, str]]:
    docs = []
    for path in DATA_DIR.glob("*.md"):
        text = path.read_text()
        for i, chunk in enumerate([p.strip() for p in text.split("\n\n") if p.strip()]):
            docs.append({"source": path.name, "chunk_id": str(i), "text": chunk})
    return docs

def retrieve(query: str, top_k: int = 3) -> List[Dict[str, str]]:
    query_lower = query.lower()
    docs = load_documents()
    scored = []
    for doc in docs:
        text_lower = doc["text"].lower()
        score = sum(1 for token in query_lower.split() if token.strip("?.!,") in text_lower)
        for words in KEYWORDS.values():
            score += sum(1 for word in words if word in query_lower and word in text_lower)
        scored.append((score, doc))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [doc for score, doc in scored[:top_k] if score > 0] or docs[:top_k]
