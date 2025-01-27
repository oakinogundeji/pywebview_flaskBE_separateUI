from flask import Flask
from flask_cors import CORS

chat_history = {}


def startUp():
    print("Starting backend initialization...")


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    CORS(app)

    return app


if __name__ == "__main__":
    startUp()
    app = create_app()
    app.run(host="localhost", port=8080)
