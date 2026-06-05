class DemoVectorStore:
    def __init__(self):
        self.items = []

    def add(self, text: str, metadata: dict):
        self.items.append({"text": text, "metadata": metadata})

    def search(self, query: str, top_k: int = 3):
        return self.items[:top_k]
