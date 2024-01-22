# SELF-STUDY EXERCISE - SATISFY THESE UNIT TESTS
#
# from app.tests.base import BaseTestCase
# from app.tests.api_tests.helpers import create_user
# from app.server.api.models.user_model import User
# from app.server.api.models.base import DBInterface
# from app.database import db
#
#
# class UserModelTests(BaseTestCase):
#     """
#     Test integration of User model in Database.
#
#     Methods:
#         test_user_created - Test user created successfully.
#         test_update_user - Test user updated successfully.
#         test_delete_user - Test user deleted successfully.
#
#     """
#
#     def test_user_created(self, app):
#         """
#         Test User is created successfully.
#
#         id: INTEGER PRIMARY KEY AUTOINCREMENT
#         name: VARCHAR(150)
#         username: VARCHAR(60)
#         email: VARCHAR(100)
#         phone: VARCHAR(50)
#         """
#
#         with app.app_context():
#             user = create_user()
#             self.interface.add_to_db(user)
#
#             users = User.query.all()
#             self.assertEqual(len(users), 1)
#             self.assertEqual(users[0].name, "Test User")
#             self.assertEqual(users[0].username, "testusername")
#             self.assertEqual(users[0].email, "test@example.com")
#             self.assertEqual(users[0].phone, "1234567890")
#
#     def test_add_user_existing_username_raises_error(self, app):
#         """Test that an error is raised in insertion attempt when username already exists."""
#
#         with app.app_context():
#             user = create_user()
#
#             self.interface.add_to_db(user)
#
#             # Create second user with exactly the same details
#             duplicate_user = create_user()
#
#             self.interface.add_to_db(user)
#
#             # Database should still only contain one record with username of 'testusername'.
#             users = User.query.filter_by(username="testusername").all()
#             self.assertEqual(len(users), 1)
#
#     def test_update_user_with_invalid_key_raises_error(self, app):
#         """Test that adding a new key on user update is forbidden, and ValueError is thrown."""
#
#         with app.app_context():
#             user = create_user()
#
#             self.interface.add_to_db(user)
#
#             user = User.query.filter_by(name="Test User").first()
#             update_dict = {
#                 "wrong_key": 12345,
#                 "email": "newemail@example.com",
#             }
#
#             with self.assertRaises(ValueError):
#                 self.interface.update_object(user, update_dict)
#                 updated_user = User.query.filter_by(name="Test User").first()
#                 self.assertNotIn(updated_user, "wrong_key")
#
#     def test_update_user(self, app):
#         """Test updating user with valid details is successful."""
#         with app.app_context():
#             user = create_user()
#
#             self.interface.add_to_db(user)
#
#             retrieved_user = self.interface.get_object(User, username=user.username)
#
#             update_dict = {
#                 "name": "New Name",
#                 "email": "newemail@example.com",
#             }
#
#             self.interface.update_object(retrieved_user, update_dict)
#
#             updated_user = self.interface.get_object(User, username=user.username)
#
#             self.assertTrue(isinstance(updated_user, User))
#             self.assertEqual(updated_user.name, "New Name")
#             self.assertEqual(updated_user.email, "newemail@example.com")
#             self.assertEqual(updated_user.phone, "1234567890")
#             self.assertEqual(updated_user.username, "testusername")
#
#     def test_delete_user(self, app):
#         """Test deleting a user"""
#
#         with app.app_context():
#             user = create_user()
#
#             self.interface.add_to_db(user)
#
#             users = User.query.all()
#             self.assertEqual(len(users), 1)
#
#             user = self.interface.get_object(User, username=user.username)
#             self.interface.remove_from_db(user)
#
#             users = User.query.all()
#             self.assertEqual(len(users), 0)
