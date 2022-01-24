import requests
import random

data = {
    "name": str(random.randint(0, 10000))
}

print(requests.post("http://127.0.0.1:5000/now", json=data).json())
