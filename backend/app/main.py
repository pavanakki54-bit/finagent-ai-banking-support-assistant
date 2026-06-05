from fastapi import FastAPI
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.agents.banking_agent import run_banking_agent
from app.rag.ingest import ingest_documents
from app.services.response_service import format_sources

app = FastAPI(title="FinAgent AI", version="1.0.0")

@app.get("/health")
def health():
    return {"status": "healthy", "service": "FinAgent AI"}

@app.post("/ingest")
def ingest():
    return ingest_documents()

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = run_banking_agent(request.user_id, request.message, request.payment_id)
    result["sources"] = format_sources(result["sources"])
    return result

@app.get("/tickets")
def tickets():
    return {"message": "Tickets are created in-memory for this portfolio demo."}
