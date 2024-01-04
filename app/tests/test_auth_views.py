"""Unit Tests for Authorization Views"""

from app.tests.base import ViewTestCase
from app.server.auth.models.user.user_model import User
from app.database import db

import json


class AuthViewTests(ViewTestCase):
    """
    Test various auth views.
    """
    def test_register_successful(self, app,  client):
        """Test making POST request to register user successful"""

        test_user = {
            "email": "testing@example.com",
            "password": "testpass123"
        }

        res = client.post("/auth_api/", data=json.dumps(test_user), content_type="application/json")
        self.assertEqual(res.status_code, 201)

        with app.app_context():
            user = db.session.execute(db.select(User).filter_by(email=test_user["email"])).scalar_one()
            self.assertTrue(user is not None)
            self.assertEqual(user.email, test_user["email"])

            data = json.loads(res.data)
            self.assertIn("token", data)

    def test_register_incomplete_data_raises_error(self, app, client):
        """Test making POST request without email specified raises error."""

        test_user_no_email = {
            "password": "testpass123"
        }

        res = client.post("/auth_api/", data=json.dumps(test_user_no_email), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        data = json.loads(res.data)
        self.assertEqual(data["msg"], "Please provide both an email and a password")

        test_user_no_password = {
            "email": "test@example.com"
        }

        res = client.post("/auth_api/", data=json.dumps(test_user_no_password), content_type="application/json")
        self.assertEqual(res.status_code,400)
        self.assertEqual(data["msg"], "Please provide both an email and a password")

    def test_register_existing_email_raises_error(self, app, client):
        """Test HTTP 400 Error returned if user attempts registration with existing email."""

        with app.app_context():
            db.session.add(User(email="test@example.com", password="testpass123"))
            db.session.commit()

        new_user = {
            "email": "test@example.com",
            "password": "testpass123"
        }

        res = client.post("/auth_api/", data=json.dumps(new_user), content_type="application/json")
        self.assertEqual(res.status_code, 400)
        data = json.loads(res.data)
        self.assertEqual(data["msg"], "Email address already exists.")

    # def test_logout(self):
    #     pass
    #
    # def test_update_user(self):
    #     pass
