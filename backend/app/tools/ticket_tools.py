from datetime import datetime

def create_support_ticket(reason: str, user_message: str) -> dict:
    ticket_id = "CASE-" + datetime.utcnow().strftime("%Y%m%d%H%M%S")
    return {"ticket_id": ticket_id, "reason": reason, "status": "Created", "summary": user_message[:180]}
