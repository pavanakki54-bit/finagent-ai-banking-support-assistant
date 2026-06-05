def is_grounded(answer: str, sources: list[dict]) -> bool:
    return bool(answer.strip()) and len(sources) > 0
