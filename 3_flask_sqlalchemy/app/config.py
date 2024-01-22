"""
Configurations for following environments:

- Test
- Dev
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = "postgresql://postgres:@localhost/"
database_name = "flask_workshop_3_db"


class BaseConfig:
    """Base Configuration. Superclass of Dev and Test config."""
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
    PRESERVE_CONTEXT_ON_EXCEPTION = False
