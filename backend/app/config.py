from pydantic import BaseModel

class Settings(BaseModel):
    app_name: str = "FinAgent AI"
    confidence_threshold: float = 0.72
    top_k: int = 3

settings = Settings()
