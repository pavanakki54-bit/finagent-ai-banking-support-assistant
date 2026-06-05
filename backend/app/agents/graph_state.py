from typing import TypedDict, Optional, List, Dict, Any

class AgentState(TypedDict, total=False):
    user_id: str
    message: str
    payment_id: Optional[str]
    intent: str
    sources: List[Dict[str, str]]
    tool_result: Optional[Dict[str, Any]]
    answer: str
    confidence: float
    handoff_required: bool
    ticket_id: Optional[str]
