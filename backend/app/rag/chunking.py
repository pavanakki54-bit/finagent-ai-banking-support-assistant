def chunk_text(text: str, max_chars: int = 600) -> list[str]:
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []
    current = ""
    for paragraph in paragraphs:
        if len(current) + len(paragraph) > max_chars:
            chunks.append(current.strip())
            current = paragraph
        else:
            current += "\n\n" + paragraph
    if current.strip():
        chunks.append(current.strip())
    return chunks
