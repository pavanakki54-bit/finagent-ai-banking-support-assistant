from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class ChatRequest(BaseModel):
    user_id: str = Field(default="demo-user")
    message: str
    payment_id: Optional[str] = None

class SourceChunk(BaseModel):
    source: str
    text: str

class ChatResponse(BaseModel):
    intent: str
    answer: str
    confidence: float
    sources: List[SourceChunk] = []
    tool_result: Optional[Dict[str, Any]] = None
    handoff_required: bool = False
    ticket_id: Optional[str] = None
