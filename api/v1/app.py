#!/usr/bin/python3
"""
script declares method for our app variable and port and host
first endpoint (route) will be to return the status of your API
"""
from flask import Flask, make_response, jsonify
from models import storage
from app.v1.views import app_views
from flask import Flask, Blueprint, jsonify, make_response
from flask_cors import CORS
import os

# creating a variable app an instance of Flask
app = Flask(__name__)
CORS(app, origins="0.0.0.0")

# register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views, url_prefix="/api/v1")
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close(cntxt):
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    return {"error": "Not found"}, 404


@app.errorhandler(400)
def page_not_found(e):
    message = e.description
    return message, 400


@app.teardown_appcontext
def close(ctx):
    storage.close()


if os.getenv("HBNB_API_HOST"):
    host = os.getenv("HBNB_API_HOST")
else:
    host = "0.0.0.0"

if os.getenv("HBNB_API_HOST"):
    port = int(os.getenv("HBNB_API_PORT"))
else:
    port = 5000


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
