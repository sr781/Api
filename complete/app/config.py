import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = "postgresql://postgres:@localhost/"
database_name = "flask_jwt_auth"

from datetime import timedelta


class BaseConfig:
    """Base Configuration."""
    SECRET_KEY = os.getenv("FLASK_SECRET", "pass")
    DEBUG = False
    JWT_COOKIE_SECURE = False
    JWT_SECRET_KEY = "changeme"
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=10)


class DevConfig(BaseConfig):
    """Development Configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestConfig(BaseConfig):
    """Testing Configuration"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + "_test"
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(seconds=10)
