from app.tests.base import ViewTestCase
# from app.server.api.models.address_model import Address


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

