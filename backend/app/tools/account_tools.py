import json
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[3] / "mock_data" / "accounts.json"

def get_account_summary(user_id: str = "demo-user") -> dict:
    accounts = json.loads(DATA_PATH.read_text())
    return accounts.get(user_id, {"user_id": user_id, "account_type": "Demo Checking", "status": "Active"})
