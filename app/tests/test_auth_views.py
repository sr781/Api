"""Unit Tests for Authorization Views"""

from app.tests.base import ViewTestCase
from app.server.auth.models.user.user_model import User
from app.database import db
from app.manage import app

import json


class AuthViewTests(ViewTestCase):
    """
    Test various auth views.
    """
    def test_register_successful(self, app,  client):
        """Test making POST request to register user successful"""

        test_user = {
            "email": "testinglklkljsdfs@example.com",
            "password": "testpass123"
        }

        res = client.post("/auth_api/", data=json.dumps(test_user), content_type="application/json")
        self.assertEqual(res.status_code, 201)

        with app.app_context():
            user = db.session.execute(db.select(User).filter_by(email=test_user["email"])).scalar_one()
            self.assertTrue(user is not None)
            self.assertEqual(user.email, test_user["email"])
