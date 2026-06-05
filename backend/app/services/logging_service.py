def log_event(event_name: str, payload: dict):
    print({"event": event_name, **payload})
