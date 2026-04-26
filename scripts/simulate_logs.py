import requests
import time
import random

API_URL = "http://localhost:8000/api/v1/logs/"

SERVICES = ["AuthService", "PaymentAPI", "Database", "Gateway", "Worker-1"]
LEVELS = ["INFO", "WARNING", "ERROR", "CRITICAL"]
MESSAGES = [
    "User authentication successful",
    "Database connection latency high",
    "API request timed out",
    "Invalid token received",
    "Background job completed",
    "Disk space reaching 90%",
    "Anomaly detected in traffic pattern"
]

def send_log():
    log = {
        "service_name": random.choice(SERVICES),
        "level": random.choice(LEVELS),
        "message": random.choice(MESSAGES),
        "metadata_json": "{}",
        "is_anomaly": random.random() < 0.1
    }
    try:
        response = requests.post(API_URL, json=log)
        print(f"Sent: {log['level']} - {log['service_name']} - {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Starting log simulation... Press Ctrl+C to stop.")
    while True:
        send_log()
        time.sleep(random.uniform(1, 5))
