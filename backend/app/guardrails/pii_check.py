import re

def contains_sensitive_data(text: str) -> bool:
    patterns = [r"\b\d{3}-\d{2}-\d{4}\b", r"\b\d{16}\b", r"\b\d{9}\b"]
    return any(re.search(pattern, text) for pattern in patterns)
