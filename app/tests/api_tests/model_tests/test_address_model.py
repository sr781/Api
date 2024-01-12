from app.tests.base import BaseTestCase
from app.tests.api_tests.helpers import create_user, create_address
from app.server.api.models.address_model import Address
from app.server.api.models.user_model import User

from app.database import db


class AddressModelTests(BaseTestCase):
    """
    Test integration of Address model in Database

    Methods:
        test_create_address - Test address created successfully.
        test_update_address - Test address updated successfully.
        test_delete_address - Test address deleted successfully.
        TODO: test_address_assigned_to_expected_user - Test address bears relationship with expected user only.
        TODO: test_address_cascade_on_user_delete - Test address deleted when related user removed from DB.
    """

    def test_create_address(self, app):
        """Test creating an address"""

        with app.app_context():
            user = create_user()
            user.insert()

            user = User.query.filter_by(id=1).first()

            address = create_address(user.id)

            address.insert()

            addresses = Address.query.all()
            self.assertEqual(len(addresses), 1)
            self.assertEqual(addresses[0].street, "Test Street")
            self.assertEqual(addresses[0].suite, "Test Suite")
            self.assertEqual(addresses[0].city, "Test City")
            self.assertEqual(addresses[0].zipcode, "T35TZP")
            self.assertEqual(addresses[0].lat, "-3.01244")
            self.assertEqual(addresses[0].long, "24.34234")

    def test_update_address(self, app):
        """Test updating an address"""

        with app.app_context():
            user = create_user()
            user.insert()
            user_with_address = User.query.filter_by(id=1).first()
            address = create_address(user_with_address.id)
            address.insert()

            address_to_update = Address.query.filter_by(user_id=user.id).first()

            address_to_update.street = "New Street"
            address_to_update.suite = "New Suite"
            address_to_update.city = "New City"
            address_to_update.lat = "-3.1000"

            db.session.commit()

            updated_address = Address.query.filter_by(user_id=user.id).first()

            # Street, Suite, City updated only.
            self.assertEqual(updated_address.street, "New Street")
            self.assertEqual(updated_address.suite, "New Suite")
            self.assertEqual(updated_address.city, "New City")
            self.assertEqual(updated_address.zipcode, "T35TZP")
            self.assertEqual(updated_address.lat, "-3.1000")
            self.assertEqual(updated_address.long, "24.34234")

    def test_delete_address(self, app):
        """Test deleting an address."""

        with app.app_context():
            user = create_user()
            user.insert()
            user_with_address = User.query.filter_by(id=1).first()
            address = create_address(user_with_address.id)
            address.insert()

            address_to_delete = Address.query.filter_by(user_id=user.id).first()

            db.session.delete(address_to_delete)
            db.session.commit()

            addresses = Address.query.all()
            self.assertEqual(len(addresses), 0)

    def test_address_assigned_to_user(self, app):
        """Test that an address is able to be retrieved using the associated user's ID."""

        with app.app_context():
            user = create_user()
            user.insert()
            user_with_address = User.query.filter_by(id=1).first()

            address = create_address(user_with_address.id)
            address.insert()

            user_address = Address.query.filter_by(user_id=user.id).first()
            self.assertEqual(user_address.user_id, user.id)

    def test_address_cascade_on_user_delete(self, app):
        """Test that an address is able to be retrieved using the associated user's ID."""

        with app.app_context():
            user = create_user()
            user.insert()
            user_with_address = User.query.filter_by(id=1).first()

            address = create_address(user_with_address.id)
            address.insert()

            address_list = Address.query.all()
            self.assertEqual(len(address_list), 1)

            user_to_remove = User.get_user(user.username)
            User.remove(user_to_remove)
            new_address_list = Address.query.all()
            self.assertEqual(len(new_address_list), 0)
