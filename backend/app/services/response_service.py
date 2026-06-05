def format_sources(sources: list[dict]) -> list[dict]:
    return [{"source": s["source"], "text": s["text"][:300]} for s in sources]
