import requests

# SERVER_IP = "127.0.0.1"
SERVER_IP = "192.168.88.216"
SERVER_URL = f"http://{SERVER_IP}:5000"

name = input("Enter your name, please: ")
resp = requests.post(f"{SERVER_URL}/auth", json={"name": name})
print("Status: ", resp.json()["status"])

# command = input("Enter command or message: ")
command = '''
               .-.
         .-'``(   )
      ,`\ \    `-`.
     /   \ '``-.   `   
   .-.  ,       `___: 
  (   ) :        ___  
   `-`  `       ,   :
     \   / ,..-`   ,
      `./ /    .-.`
         `-..-(   )
               `-`
'''

while True:
    if command == "update":
        messages = requests.get(SERVER_URL).json()["data"]
        for message in messages:
            print(message["ts"], message["name"])
            print(message["message"])
    else:
        requests.post(f"{SERVER_URL}/send", json={"text": command})
