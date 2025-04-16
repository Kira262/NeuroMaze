# backend_client.py
"""
Handles communication with the FastAPI backend for difficulty adjustment.
"""
import requests
import random

def send_to_backend(emotion):
    """Send emotion and dummy stats to backend, return difficulty and feedback."""
    payload = {
        "puzzle_time": round(random.uniform(30, 120), 2),
        "error_rate": round(random.uniform(0, 1), 2),
        "emotion": emotion,
    }
    print("[DEBUG] Sending payload:", payload)
    try:
        response = requests.post(
            "http://127.0.0.1:8000/adjust-difficulty/", json=payload
        )
        print("[DEBUG] Got response:", response.text)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Backend not reachable: {e}")
        return {"difficulty": "Normal", "feedback": "Offline mode"}
