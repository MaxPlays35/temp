from flask import Flask, request, jsonify

last_name = ""

app = Flask(__name__)


@app.route('/now', methods=["POST"])
def index():
    global last_name
    ln = last_name
    last_name = request.json["name"]
    return jsonify(data=ln)


if __name__ == "__main__":
    app.run()
