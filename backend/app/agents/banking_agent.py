from app.config import settings
from app.rag.retriever import retrieve
from app.tools.payment_tools import check_payment_status
from app.tools.account_tools import get_account_summary
from app.tools.eligibility_tools import check_eligibility
from app.tools.ticket_tools import create_support_ticket
from app.guardrails.pii_check import contains_sensitive_data
from app.guardrails.confidence_check import is_confident
from app.guardrails.grounding_check import is_grounded
from app.services.llm_service import generate_answer
from app.services.logging_service import log_event


def detect_intent(message: str) -> str:
    text = message.lower()
    if any(word in text for word in ["payment", "ach", "transfer", "pending", "delayed"]):
        return "payment_inquiry"
    if any(word in text for word in ["account", "balance", "profile"]):
        return "account_question"
    if any(word in text for word in ["eligible", "eligibility", "qualify", "loan"]):
        return "eligibility_check"
    if any(word in text for word in ["human", "agent", "representative", "support"]):
        return "human_support"
    return "policy_faq"


def run_banking_agent(user_id: str, message: str, payment_id: str | None = None) -> dict:
    intent = detect_intent(message)
    sources = retrieve(message, top_k=settings.top_k)
    tool_result = None

    if intent == "payment_inquiry":
        tool_result = check_payment_status(payment_id or "PAY-1001")
    elif intent == "account_question":
        tool_result = get_account_summary(user_id)
    elif intent == "eligibility_check":
        tool_result = check_eligibility(user_id)

    answer, confidence = generate_answer(message, intent, sources, tool_result)
    pii_risk = contains_sensitive_data(message + " " + answer)
    grounded = is_grounded(answer, sources)
    confident = is_confident(confidence, settings.confidence_threshold)
    handoff_required = pii_risk or not grounded or not confident or intent == "human_support"
    ticket_id = None

    if handoff_required:
        ticket = create_support_ticket("Low confidence, sensitive data, or human support requested", message)
        ticket_id = ticket["ticket_id"]
        answer = "I created a support ticket for human review instead of returning an uncertain or sensitive response."

    log_event("agent_completed", {"intent": intent, "confidence": confidence, "handoff": handoff_required})

    return {
        "intent": intent,
        "answer": answer,
        "confidence": confidence,
        "sources": sources,
        "tool_result": tool_result,
        "handoff_required": handoff_required,
        "ticket_id": ticket_id,
    }
