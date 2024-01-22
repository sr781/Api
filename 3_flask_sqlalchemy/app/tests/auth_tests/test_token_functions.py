from app.tests.base import ViewTestCase
import json
import time
from datetime import timedelta


# class TokenTests(ViewTestCase):
#     """
#     Tests for Flask JWT Extended token API.
#
#     Methods:
#         test_jwt_token_refreshed - Test JWT refreshes successfully.
#
#         test_jwt_token_not_refreshed_if_request_made_within_expiry_delta -
#             Test that token isn't refreshed if a request is made within the JWT expiration delta.
#
#
#     """
#
#     def test_jwt_token_refreshed(self, app, client):
#         """Test that token refreshes successfully after given time delta."""
#
#         with self.app_context:
#             # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=10)
#             test_user = {
#                 "email": "test@example.com",
#                 "password": "testpass123"
#             }
#             res = client.post("/auth_api/", data=json.dumps(test_user), content_type="application/json")
#
#             self.assertEqual(res.status_code, 201)
#
#             curr_token_cookie = client.get_cookie("access_token_cookie")
#
#             # JWT access token expires after 10 seconds in testing environment.
#             # Token refreshes after every request if timestamp is within at least 8 seconds
#             # of JWT access token expiration.
#             res = client.get(f"/auth_api/{1}")
#
#             # 8 + 3 = 11
#             # 11 > 10 (seconds) === JWT expired. Refresh it.
#             time.sleep(3)
#             res = client.get(f"/auth_api/{1}")
#             new_token_cookie = client.get_cookie("access_token_cookie")
#             self.assertEqual(res.status_code, 200)
#
#             # The new token cookie should not match the previous.
#             self.assertNotEqual(curr_token_cookie, new_token_cookie)
#
#             res = client.get(f"/auth_api/{1}")
#             self.assertEqual(res.status_code, 200)
#
#     def test_jwt_token_not_refreshed_if_request_made_within_expiry_delta(self, app, client):
#         """
#         Test that token isn't refreshed if a request is made within the JWT expiration delta.
#         """
#
#         with self.app_context:
#             app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=20)
#             test_user = {
#                 "email": "test@example.com",
#                 "password": "testpass123"
#             }
#             res = client.post("/auth_api/", data=json.dumps(test_user), content_type="application/json")
#
#             self.assertEqual(res.status_code, 201)
#
#             curr_token_cookie = client.get_cookie("access_token_cookie")
#
#             # JWT access token expires after 10 seconds in testing environment.
#             # Token refreshes after every request if timestamp is within at least 8 seconds
#             # of JWT access token expiration.
#
#             # 8 + 1 = 9
#             # 9 < 10 (seconds) === JWT not expired.
#             time.sleep(1)
#             res = client.get(f"/auth_api/{1}")
#             new_token_cookie = client.get_cookie("access_token_cookie")
#             self.assertEqual(res.status_code, 200)
#
#             # New token should match previous.
#             self.assertEqual(curr_token_cookie, new_token_cookie)
#
#     def test_jwt_token_revoked_if_request_made_after_expiry(self, app, client):
#         """Test that a JWT token is revoked if request is made after expiration of JWT access token."""
#
#         with self.app_context:
#             app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(seconds=2)
#             test_user = {
#                 "email": "test@example.com",
#                 "password": "testpass123"
#             }
#             res = client.post("/auth_api/", data=json.dumps(test_user), content_type="application/json")
#
#             self.assertEqual(res.status_code, 201)
#
#             time.sleep(3)
#             res = client.get(f"/auth_api/{1}")
#             data = json.loads(res.data)
#
#             self.assertEqual(res.status_code, 401)
#             self.assertEqual(data["msg"], "Token has expired")
