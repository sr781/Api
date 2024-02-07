"""Index Blueprint. To test and make sure everything works"""
from flask import Blueprint

index_test_blueprint = Blueprint("index", __name__) #initialises a Blueprint from flask

@index_test_blueprint.route("/", methods=["GET"])
def test_index():
    return "Hello, this is my project!"