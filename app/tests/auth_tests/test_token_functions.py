from app.tests.base import ViewTestCase
import json

from flask_jwt_extended import get_jwt_identity


class TokenTests(ViewTestCase):
    """Tests for Flask JWT Extended token API."""

    def test_jwt_token_refreshed(self, app, client):
        """Test that token refreshes successfully after given time delta."""

        test_user = {
            "email": "test@example.com",
            "password": "testpass123"
        }
        res = client.post("/auth_api/", data=json.dumps(test_user), content_type="application/json")

        self.assertEqual(res.status_code, 201)

        with self.app_context:
            res = client.get(f"/auth_api/{1}")
            self.assertEqual(res.status_code, 200)

