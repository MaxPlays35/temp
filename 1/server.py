from flask import Flask, request, jsonify
from chat import Chat


app = Flask(__name__)
chat = Chat()

@app.post("/auth")
def auth():
    name = request.json["name"]
    ip_addr = request.remote_addr
    chat.login(ip_addr, name)

    return jsonify(status="ok"), 201

@app.post("/send")
def send():
    ip_addr = request.remote_addr
    text = request.json["text"]

    chat.add_message(ip_addr, text)

    return jsonify(status="ok")

@app.get("/")
def get_messages():
    messages = chat.get_messages()

    return jsonify(status="ok", data=messages)


if __name__ == "__main__":
    app.run()
