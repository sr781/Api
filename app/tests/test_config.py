from typing import Union, Iterator

import unittest
from flask_unittest import AppTestCase
from flask import Flask, current_app
from app.server import app as flask_app


class TestDevConfig(AppTestCase):
    def create_app(self) -> Union[Flask, Iterator[Flask]]:
        flask_app.config.from_object("app.server.config.DevConfig")
        return flask_app

    def test_app_is_development(self, app):
        self.assertTrue(flask_app.config["SECRET_KEY"], "pass")
        self.assertTrue(flask_app.config["DEBUG"] is True)
        self.assertFalse(current_app is None)
        self.assertEqual(app.config["SQLALCHEMY_DATABASE_URI"], "postgresql://postgres:@localhost/flask_jwt_auth")


if __name__ == "__main__":
    unittest.main()
