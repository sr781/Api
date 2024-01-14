from app.tests.base import ViewTestCase
from app.server.api.models.address_model import Address
from app.server.api.models.user_model import User
from app.tests.api_tests.helpers import create_user, create_address
from app.server.auth.models.user.user_model import AuthUser
from app.database import db
import json


def create_auth_user(post_request):
    """Helper method to create a test auth user."""
    auth_dict = {
        "email": "testauth@example.com",
        "password": "testpass123"
    }

    return post_request(
        "/auth_api/", data=json.dumps(auth_dict), content_type="application/json")


class UserViewTests(ViewTestCase):
    """
    Test various HTTP endpoints of User view.

    Methods:
        test_get_users - Test all users returned with 200 response.
        test_get_users_error_unauthorized - Test 401 response for unauthorized access
        test_get_user_by_id - Test user is returned with 200 response.
        test_get_user_by_id_error_unauthorized - Test 401 response for unauthorized access.
        test_post_user - Test creating a user with address (if exists) is successful
                         with 201 response.
        test_post_user_unauthorized - Test 401 response for unauthorized access.
        test_patch_user - Test updating a user returns 200, with user details successfully updated.
        test_patch_user_unauthorized - Test 401 response for unauthorized access.
        test_delete_user - Test deleting a user returns 204 response.
        test_delete_user_unauthorized - Test 401 response for unauthorized access.
    """

    def test_post_user(self, app, client):
        """Test POST request to create a user is successful."""

        with self.app_context:
            user_details = {
                "name": "Test Name",
                "username": "testusername",
                "email": "test@example.com",
                "phone": "1234567890",
                "address": {
                    "street": "Test Street",
                    "suite": "Test Suite",
                    "city": "Test City",
                    "zipcode": "T35TZP",
                    "lat": "-13.125",
                    "long": "24.009"
                }
            }

            create_auth_user(client.post)

            res = client.post("/api/user-list/", data=json.dumps(user_details), content_type="application/json")
            self.assertEqual(res.status_code, 201)

            user = self.interface.get_object(User, id=1)
            self.assertEqual(user.name, user_details["name"])
            self.assertEqual(user.username, user_details["username"])
            self.assertEqual(user.email, user_details["email"])
            self.assertEqual(user.phone, user_details["phone"])

            address = self.interface.get_object(Address, id=1)
            self.assertEqual(address.user_id, user.id)
            self.assertEqual(address.street, user_details["address"]["street"])
            self.assertEqual(address.suite, user_details["address"]["suite"])
            self.assertEqual(address.city, user_details["address"]["city"])
            self.assertEqual(address.zipcode, user_details["address"]["zipcode"])
            self.assertEqual(address.lat, user_details["address"]["lat"])
            self.assertEqual(address.long, user_details["address"]["long"])

    def test_post_user_unauthorized(self, app, client):
        """Test 401 error returned when authorized POST request made."""

        with self.app_context:
            user_details = {
                "name": "Test Name",
                "username": "testusername",
                "email": "test@example.com",
                "phone": "1234567890",
                "address": {
                    "street": "Test Street",
                    "suite": "Test Suite",
                    "city": "Test City",
                    "zipcode": "T35TZP",
                    "lat": "-13.125",
                    "long": "24.009"
                }
            }

            res = client.post("/api/user-list/", data=json.dumps(user_details), content_type="application/json")
            data = json.loads(res.data)

            self.assertEqual(res.status_code, 401)
            self.assertEqual(data["msg"], "Please login.")

    def test_get_users(self, app, client):
        """Test GET request to get list of users is successful."""

        test_user_1 = create_user()
        self.interface.add_to_db(test_user_1)

        test_user_2 = create_user(email="testuser2@example.com")
        self.interface.add_to_db(test_user_2)

        test_user_3 = create_user(email="testuser3@example.com")
        self.interface.add_to_db(test_user_3)

        test_address_1 = create_address(test_user_1.id)
        self.interface.add_to_db(test_address_1)

        test_address_2 = create_address(test_user_2.id, street="Another Test Street")
        self.interface.add_to_db(test_address_2)

        test_address_3 = create_address(test_user_2.id)
        self.interface.add_to_db(test_address_3)

        create_auth_user(client.post)

        res = client.get("/api/user-list/")
        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)
        self.assertEqual(len(data["data"]), 3)

    def test_get_users_unauthorized(self, app, client):
        """Test unauthorized GET request to User List API returns 401."""

        res = client.get("/api/user-list/")
        self.assertEqual(res.status_code, 401)

    def test_get_user_by_id(self, app, client):
        """Test GET request to return single user returns 200."""
        test_user_1 = create_user()
        self.interface.add_to_db(test_user_1)

        test_address_1 = create_address(test_user_1.id)
        self.interface.add_to_db(test_address_1)

        create_auth_user(client.post)

        res = client.get(f"/api/user-item/{test_user_1.id}")

        self.assertEqual(res.status_code, 200)

        data = json.loads(res.data)

        self.assertEqual(data["data"]["id"], 1)
        self.assertEqual(data["data"]["name"], "Test User")
        self.assertEqual(data["data"]["username"], "testusername")
        self.assertEqual(data["data"]["email"], "test@example.com")
        self.assertEqual(data["data"]["phone"], "1234567890")
        self.assertEqual(data["data"]["addresses"][0]["street"], "Test Street")
        self.assertEqual(data["data"]["addresses"][0]["suite"], "Test Suite")
        self.assertEqual(data["data"]["addresses"][0]["zipcode"], "T35TZP")
        self.assertEqual(data["data"]["addresses"][0]["lat"], "-3.01244")
        self.assertEqual(data["data"]["addresses"][0]["long"], "24.34234")

    def test_get_user_by_id_unauthorized(self, app, client):
        """Test 401 error returned when unauthorized GET request made for single user."""

        test_user_1 = create_user()
        self.interface.add_to_db(test_user_1)

        res = client.get(f"/api/user-item/{test_user_1.id}")
        self.assertEqual(res.status_code, 401)

        data = json.loads(res.data)
        self.assertEqual(data["msg"], "Please login.")
    #
    # def test_patch_user(self):
    #     pass
    #
    # def test_patch_user_unauthorized(self):
    #     pass
    #
    # def test_delete_user(self):
    #     pass
    #
    # def test_delete_user_unauthorized(self):
    #     pass

