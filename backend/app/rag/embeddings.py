def embed_text(text: str) -> list[float]:
    # Placeholder deterministic embedding for portfolio demo.
    return [float((sum(ord(c) for c in text) % 1000) / 1000)]
