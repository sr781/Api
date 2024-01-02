import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = "postgresql://postgres:@localhost/"
database_name = "flask_jwt_auth"


class BaseConfig:
    """Base Configuration."""

    SECRET_KEY = os.getenv("FLASK_SECRET", "pass")
    DEBUG = False


class DevConfig(BaseConfig):
    """Development Configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestConfig(BaseConfig):
    """Testing Configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + "_test"
