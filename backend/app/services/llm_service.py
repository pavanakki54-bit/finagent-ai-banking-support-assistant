def generate_answer(message: str, intent: str, sources: list[dict], tool_result: dict | None) -> tuple[str, float]:
    source_text = sources[0]["text"] if sources else "No policy context found."
    if intent == "payment_inquiry" and tool_result:
        answer = (
            f"Your payment status is {tool_result.get('status', 'unknown')}. "
            f"Reason: {tool_result.get('reason', 'Not available')}. "
            f"Based on the policy context: {source_text[:220]}"
        )
        return answer, 0.91
    if intent == "account_question" and tool_result:
        answer = f"Your demo account is {tool_result.get('status', 'available')}. Based on account policy: {source_text[:220]}"
        return answer, 0.86
    answer = f"Based on the available banking policy context: {source_text[:350]}"
    return answer, 0.78
