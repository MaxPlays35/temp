import requests

resp = requests.post("http://192.168.88.254:4561/me", json={
    "surname": "Mikhailov"
})

print(resp.text)
