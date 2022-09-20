#!/usr/bin/python3
"""index.py """


from api.v1.views import app_views
from flask import jsonify
from models import storage
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes_rel = {"Amenity": "amenities", "City": "cities", "Place": "places",
               "Review": "reviews", "State": "states", "User": "users"}


@app_views.route('/status', strict_slashes=False)
def status():
    """ returns a JSON """
    response = {'status':'OK'}
    return jsonify(response)


@app_views.route('/stats', strict_slashes=False)
def stats():
    """ number of each objects by type"""
    response = jsonify(amenties=storage.count(Amenity),
                       cities=storage.count(City),
                       places=storage.count(Place),
                       reviews=storage.count(Review),
                       states=storage.count(State),
                       users=storage.count(User))
    
    return jsonify(stat)
