from flask_unittest import AppTestCase, AppClientTestCase
from app.factory import create_app
from app.database import db
from typing import Union, Iterator
from flask import Flask
from flask import g


class BaseTestCase(AppTestCase):
    def create_app(self) -> Union[Flask, Iterator[Flask]]:
        app = create_app()
        return app

    def setUp(self, app):
        with app.app_context():
            db.create_all()
            db.session.commit()

    def tearDown(self, app):
        with app.app_context():
            db.session.remove()
            db.drop_all()
            db.session.close()


class ViewTestCase(AppClientTestCase):
    """Base class for View Test Cases"""

    def create_app(self):
        app = create_app()
        return app

    def setUp(self, app, client):
        self.app_context = app.app_context()
        self.app_context.push()

        db.create_all()
        db.session.commit()

    def tearDown(self, app, client):
        db.session.remove()
        db.drop_all()
        db.session.close()
        self.app_context.pop()
