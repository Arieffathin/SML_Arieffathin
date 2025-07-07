import requests
import json

url = "http://127.0.0.1:5002/invocations"  

payload = {
    "columns": ["feature1", "feature2", "feature3", "feature4"],
    "data": [
        [1.0, 2.0, 3.0, 4.0]
    ]
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print("Status Code:", response.status_code)
print("Response:", response.json())
