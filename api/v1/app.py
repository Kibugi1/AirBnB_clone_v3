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


if os.getenv("HBNB_API_HOST"):
    host = os.getenv("HBNB_API_HOST")
else:
    host = "0.0.0.0"

if os.getenv("HBNB_API_HOST"):
    port = int(os.getenv("HBNB_API_PORT"))
else:
    port = 5000


@app.errorhandler(404)
def not_found(error):
    '''
    return JSON formatted 404 status code response
    '''
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(host=getenv("HBNB_API_HOST", "0.0.0.0"),
            port=int(getenv("HBNB_API_PORT", "5000")), threaded=True)
