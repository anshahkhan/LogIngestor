import requests

log = {
    "service": "payment-service",
    "level": "ERROR",
    "message": "Transaction failed due to timeout."
}

res = requests.post("http://127.0.0.1:8000/log", json=log)
print(res.json())
