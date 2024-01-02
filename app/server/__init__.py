import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app_config = os.getenv(
    "APP_CONFIG",
    "app.server.config.DevConfig"
)

app.config.from_object(app_config)
app.testing = True

db = SQLAlchemy(app)
