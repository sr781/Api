from flask_unittest import AppTestCase, AppClientTestCase
from app.manage import app as flask_app
from app.database import db
from typing import Union, Iterator
from flask import Flask


class BaseTestCase(AppTestCase):
    def create_app(self) -> Union[Flask, Iterator[Flask]]:
        flask_app.config.from_object("app.server.config.TestConfig")
        return flask_app

    def setUp(self, app):
        with flask_app.app_context():
            db.create_all()
            db.session.commit()


    def tearDown(self, app):
        with flask_app.app_context():
            db.session.remove()
            db.drop_all()
            db.session.close()


class ViewTestCase(AppClientTestCase):
    """Base class for View Test Cases"""

    def create_app(self):
        flask_app.config.from_object("app.server.config.TestConfig")
        return flask_app

    def setUp(self, app, client):
        with flask_app.app_context():
            db.create_all()
            db.session.commit()

    def tearDown(self, app, client):
        with flask_app.app_context():
            db.session.remove()
            db.drop_all()
            db.session.close()


