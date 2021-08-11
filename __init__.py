from flask import Flask
from flask_cors import CORS


def create_app():
    flask_app = Flask('app')
    return flask_app


app = create_app()

CORS(app)
