from datetime import datetime
from flask import Flask
from flask import request
import jwt


app = Flask(__name__)

# the key for the "demo" namespace
key = "d6aa584abd36df336e1b70d777d77eaab5b976c2a119be94a9945cc52e4bffe9"


@app.route('/')
def main_route():
    token = request.headers["Authorization"].split(" ")[1]
    payload = jwt.decode(token, key, algorithms=['HS256'])
    print("Token payload", payload)
    date = datetime.fromtimestamp(payload["exp"])
    print("Token expiration date", date)
    return {"response": "ok"}
