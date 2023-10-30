#!/usr/bin/python3
"""
script declares method for our app variable and port and host
first endpoint (route) will be to return the status of your API
"""
import os
from flask import Flask
from models import storage
from app.v1.views import app_views

# creating a variable app an instance of Flask
app = Flask(__name__)

# register the blueprint app_views to your Flask instance app
app.register_blueprint(app_view, url_prefix="/api/v1")


@app.teardown_appcontext
def close(cntxt):
    storage.close()


if os.getenv("HBNB_API_HOST"):
    host = os.getenv("HBNB_API_HOST")
else:
    host = "0.0.0.0"

if os.getenv("HBNB_API_HOST"):
    port = os.getenv("HBNB_API_PORT")
else:
    port = 5000


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
