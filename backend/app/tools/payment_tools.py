import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[3] / "mock_data" / "payments.json"

def check_payment_status(payment_id: str = "PAY-1001") -> dict:
    payments = json.loads(DATA_PATH.read_text())
    return payments.get(payment_id, {"payment_id": payment_id, "status": "Not Found", "reason": "No matching synthetic record"})
