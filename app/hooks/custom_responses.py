from flask import make_response, request, jsonify


def custom_unauthorized_response():
    """Customize 401 error responses."""
    if "access_token_cookie" not in request.cookies:
        error_msg = "Please login."
        return make_response(jsonify({"msg": error_msg}), 401)
