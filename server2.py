from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.get("/")
def index():
    return str(datetime.now())


if "__main__" == __name__:
    app.run("0.0.0.0", 5000) # This unsecure, because we are listening for all network interfaces.
