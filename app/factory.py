"""Use it to create the flask app iteself"""
from flask import Flask
from .views.index import index_test_blueprint #imports the class "index_test_blueprint" to be created

def create_app():
    app = Flask(__name__)
    app.register_blueprint(index_test_blueprint)
    return app

