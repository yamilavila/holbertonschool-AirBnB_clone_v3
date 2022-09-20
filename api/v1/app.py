#!/usr/bin/python3
"""API AirBnB  """

from api.v1.views import app_views
from flask import Blueprint, Flask, jsonify
from models import storage
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={"/*": {"origins": ["0.0.0.0"]}})


@app.teardown_appcontext
def teardown(exception=None):
    """calls storage for teardown """
    storage.close()


@app.errorhandler(404)
def page_not_found(exception=None):
    """handles 404 error """
    return json_format({"error": "Not found"}), 404

if __name__ == '__main__':
    """execute functions and connections  """
    host = getenv('HBNB_API_HOST')
    if (host is None):
        host = '0.0.0.0'

    port = getenv('HBNB_API_PORT')
    if (port is None):
        port = '5000'

    app.run(host, port, threaded=True)
