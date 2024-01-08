from app.tests.base import BaseTestCase
from app.tests.api_tests.helpers import create_user
from app.server.api.models.user_model import User

from app.database import db


class UserModelTests(BaseTestCase):
    """
    Test integration of User model in Database.
    """

    def test_user_created(self, app):
        """
        Test User is created successfully.

        id: INTEGER PRIMARY KEY AUTOINCREMENT
        name: VARCHAR(150)
        username: VARCHAR(60)
        email: VARCHAR(100)
        phone: VARCHAR(50)
        """

        with app.app_context():
            create_user()

            users = User.query.all()
            self.assertEqual(len(users), 1)
            self.assertEqual(users[0].name, "Test User")
            self.assertEqual(users[0].username, "testusername")
            self.assertEqual(users[0].email, "test@example.com")
            self.assertEqual(users[0].phone, "1234567890")

    def test_update_user(self, app):
        """
        Test user updated successfully.

        API should get student by ID, and update details.
        """

        with app.app_context():
            create_user()

            user = User.query.filter_by(name="Test User").first()
            print(user)
            user.name = "New Name"
            user.email = "newemail@example.com"
            db.session.commit()

            updated_user = User.query.filter_by(name="New Name").first()
            self.assertTrue(isinstance(updated_user, User))
            self.assertEqual(updated_user.name, "New Name")
            self.assertEqual(updated_user.email, "newemail@example.com")
            self.assertEqual(updated_user.phone, "1234567890")
            self.assertEqual(updated_user.username, "testusername")

    def test_delete_user(self, app):
        """Test deleting a user"""

        with app.app_context():
            create_user()

            users = User.query.all()
            self.assertEqual(len(users), 1)

            user = db.session.get(User, ident=1)
            db.session.delete(user)
            db.session.commit()

            users = User.query.all()
            self.assertEqual(len(users), 0)
