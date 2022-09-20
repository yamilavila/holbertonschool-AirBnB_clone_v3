#!/usr/bin/python3
"""index.py """


from api.v1.views import app_views
from flask import app_views
from models import storage


classes_rel = {"Amenity": "amenities", "City": "cities", "Place": "places",
               "Review": "reviews", "State": "states", "User": "users"}

@app_views.route('/status', strict_slashes=False)
def status():
    """ returns a JSON """
    response = {'status': 'OK'}
    return jsonify(response)


@app_views.route('/stats', strict_slashes=False)
def stats():
    """Retrieves the number of each objects by type"""
    obj_count = {}

    for key, value in classes_rel.items():
        number = storage.count(key)
        obj_count[value] = number
    
    return jsonify(stat)
