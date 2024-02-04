from typing import Union, Iterator

from flask_unittest import AppTestCase
from flask import Flask
from app.factory import create_app
from app.manage import app as flask_app
from app.config import TestConfig, DevConfig


class TestDevConfig(AppTestCase):
    """
    Test appropriate configuration for Development environment.
    """
    def create_app(self) -> Union[Flask, Iterator[Flask]]:
        app = create_app(default_config=DevConfig)
        return app

    def test_app_is_development(self, app):
        self.assertTrue(flask_app.config["SECRET_KEY"], "pass")
        self.assertTrue(flask_app.config["DEBUG"] is True)
        self.assertFalse(app is None)
        self.assertEqual(app.config["SQLALCHEMY_DATABASE_URI"], "postgresql://postgres:@localhost/flask_jwt_auth")


class TestTestConfig(AppTestCase):
    """
    Test appropriate configuration for Testing environment.
    """
    def create_app(self) -> Union[Flask, Iterator[Flask]]:
        app = create_app(default_config=TestConfig)
        return app

    def test_app_is_testing(self, app):
        self.assertTrue(flask_app.config["SECRET_KEY"], "pass")
        self.assertEqual(flask_app.config["SQLALCHEMY_DATABASE_URI"], "postgresql://postgres:@localhost/flask_jwt_auth_test")
        self.assertTrue(flask_app.config["DEBUG"] is True)
