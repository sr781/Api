"""Interface to handle REST Endpoint requests."""

import requests
import time
import json

from app.conf.constants import BASE_URL #Basically "https://jsonplaceholder.typicode.com/" from the constants.py file


class ClientInterface:
    """
    Abstract object to handle GET, POST, PUT, PATCH and DELETE requests.
    """

    def __init__(self, endpoint):
        self.url = BASE_URL + endpoint

    @staticmethod
    def _make_request(method, url, data=None, headers=None):
        """Perform the request."""

        num_retries = 5
        while num_retries > 0:
            try:
                req = requests.request(
                    method=method,
                    url=url,
                    data=data,
                    headers=headers
                )
                return req
            #Below this, it is error handling
            except requests.exceptions.Timeout:
                time.sleep(1)
                num_retries -= 1
                continue
            except requests.exceptions.TooManyRedirects:
                return {
                    "error_msg": "URL may be malformed. Try a different URL."
                }
            except requests.exceptions.RequestException as e:
                raise SystemError(e)
        return {
            "error_msg": "Request timed out."
        }

    @staticmethod
    def _request_success(status_code):
        """Confirm response status code between 200 and 299."""
        return 200 <= status_code <= 299

    @staticmethod
    def _res_to_dict(response):
        """Prepare response object into dict format."""
        return {
            "status": response.status_code,
            "data": response.json()
        }

    def _prepare_response(self, req):
        if "error_msg" not in req:
            res_dict = self._res_to_dict(req)
            return res_dict
        else:
            return req

    def get_list(self):
        """Return a list of items."""
        request = self._make_request("GET", self.url)
        return self._prepare_response(request)

    def get_item(self):
        """Return a single item by item ID."""

        request = self._make_request("GET", self.url)
        return self._prepare_response(request)

    def post(self, data):
        """Create a new item."""

        request = self._make_request(
            "POST", self.url,
            data=json.dumps(data), headers={"Content-type": "application/json; charset=UTF-8"}
        )
        return self._prepare_response(request)

    def put(self, data):
        """Full update of item."""

        request = self._make_request(
            "PUT", self.url,
            data=json.dumps(data), headers={"Content-type": "application/json; charset=UTF-8"}
        )
        return self._prepare_response(request)

    def patch(self, data):
        """Partial update of item."""

        request = self._make_request(
            "PATCH", self.url,
            data=json.dumps(data), headers={"Content-type": "application/json; charset=UTF-8"}
        )
        return self._prepare_response(request)

    def delete(self):
        """Delete item."""

        request = self._make_request("DELETE", self.url)
        return self._prepare_response(request)