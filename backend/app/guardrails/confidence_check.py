def is_confident(score: float, threshold: float = 0.72) -> bool:
    return score >= threshold
