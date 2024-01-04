from flask.views import MethodView


class BaseCRUDView(MethodView):
    init_every_request = False

    def __init__(self, model):
        self.model = model

    def post(self):
        """Handle POST requests"""
        pass

    def get(self):
        """Handle GET requests"""
        pass

    def patch(self):
        """Handle PATCH requests."""
        pass

    def delete(self):
        """Handle DELETE requests."""
        pass

    def get_queryset(self):
        return self.model
