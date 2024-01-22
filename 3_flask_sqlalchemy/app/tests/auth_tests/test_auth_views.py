# """Unit Tests for Authorization Views"""
#
# from app.tests.base import ViewTestCase
# from app.server.auth.models.user.user_model import AuthUser
# from app.database import db
#
# import json
#
#
# class AuthViewTests(ViewTestCase):
#     """
#     Test various auth views.
#
#     Methods:
#         test_register_successful - Test POST request to register user returns 201.
#         test_register_incomplete_data_raises_error - Test POST request to create user with incomplete
#                                                      data (email/password) returns 400.
#         test_register_existing_email_raises_error - Test POST request to create user returns 400 if
#                                                     user with same email already exists in DB.
#         test_login - Test POST request to login returns 200.
#         test_login_with_nonexistent_email_raises_error - Test POST request with nonexistent email raises 400.
#         test_login_with_incorrect_password_raises_error - Test POST request with incorrect password raises 400.
#     """
#     def test_register_successful(self, app,  client):
#         """Test making POST request to register user successful"""
#
#         test_user = {
#             "email": "testing@example.com",
#             "password": "testpass123"
#         }
#
#         res = client.post("/auth_api/", data=json.dumps(test_user), content_type="application/json")
#         self.assertEqual(res.status_code, 201)
#
#         user = db.session.execute(db.select(AuthUser).filter_by(email=test_user["email"])).scalar_one()
#         self.assertTrue(user is not None)
#         self.assertEqual(user.email, test_user["email"])
#
#         data = json.loads(res.data)
#         self.assertEqual(data["msg"], "registration successful")
#
#     def test_register_incomplete_data_raises_error(self, app, client):
#         """Test making POST request without email specified raises error."""
#
#         test_user_no_email = {
#             "password": "testpass123"
#         }
#
#         res = client.post("/auth_api/", data=json.dumps(test_user_no_email), content_type="application/json")
#         self.assertEqual(res.status_code, 400)
#         data = json.loads(res.data)
#         self.assertEqual(data["msg"], "Please provide both an email and a password")
#
#         test_user_no_password = {
#             "email": "test@example.com"
#         }
#
#         res = client.post("/auth_api/", data=json.dumps(test_user_no_password), content_type="application/json")
#         self.assertEqual(res.status_code,400)
#         self.assertEqual(data["msg"], "Please provide both an email and a password")
#
#     def test_register_existing_email_raises_error(self, app, client):
#         """Test HTTP 400 Error returned if user attempts registration with existing email."""
#
#         db.session.add(AuthUser(email="test@example.com", password="testpass123"))
#         db.session.commit()
#
#         new_user = {
#             "email": "test@example.com",
#             "password": "testpass123"
#         }
#
#         res = client.post("/auth_api/", data=json.dumps(new_user), content_type="application/json")
#         self.assertEqual(res.status_code, 400)
#         data = json.loads(res.data)
#         self.assertEqual(data["msg"], "Email address already exists.")
#
#     def test_login(self, app, client):
#
#         test_user = {
#             "email": "test@example.com",
#             "password": "testpass123"
#         }
#
#         client.post("/auth_api/", data=json.dumps(test_user), content_type="application/json")
#
#         res = client.post("/auth_api/login", data=json.dumps(test_user), content_type="application/json")
#         data = json.loads(res.data)
#         self.assertEqual(res.status_code, 200)
#         self.assertEqual(data["id"], 1)
#         self.assertEqual(data["msg"], "Login successful.")
#
#     def test_login_with_nonexistent_email_400_error(self, app, client):
#
#         test_user = {
#             "email": "nouser@example.com",
#             "password": "testpass123"
#         }
#
#         res = client.post("/auth_api/login", data=json.dumps(test_user), content_type="application/json")
#         data = json.loads(res.data)
#         self.assertEqual(res.status_code, 400)
#         self.assertEqual(data["msg"], "Email not found. Please try again.")
#
#     def test_login_with_incorrect_password_400_error(self, app, client):
#
#         test_user = {
#             "email": "test@example.com",
#             "password": "testpass123"
#         }
#
#         client.post("/auth_api/", data=json.dumps(test_user), content_type="application/json")
#
#         test_user["password"] = "wrongpassword"
#
#         res = client.post("/auth_api/login", data=json.dumps(test_user), content_type="application/json")
#         data = json.loads(res.data)
#         self.assertEqual(res.status_code, 400)
#         self.assertEqual(data["msg"], "Incorrect password. Please try again.")
