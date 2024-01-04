"""Entry point to the application"""


import os
from app.server import create_app

app, db = create_app()

if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get("APP_DEBUG", True)
    ENVIRONMENT_PORT = os.environ.get("APP_PORT", 8000)

    app.run(host="0.0.0.0", port=443, debug=ENVIRONMENT_DEBUG)
