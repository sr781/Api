"""Base superclass"""

from app.database import db
from sqlalchemy.exc import IntegrityError, OperationalError
import time


class DBInterface:
    """Interface class to handle common DB interaction methods (add, update, delete etc)."""
    def __init__(self, model):
        self.model = model

    def add_to_db(self):
        """TODO: TEST OPERATIONAL FAILURE"""
        num_retries = 5
        db_insertion_success = False

        while num_retries > 0:
            try:
                self.commit(self.model)
                db_insertion_success = True
                break
            except OperationalError:
                num_retries -= 1
                time.sleep(1)
            except IntegrityError:
                db.session.rollback()
                return False

        if not db_insertion_success:
            return False
        return True

    @staticmethod
    def commit(obj):
        db.session.add(obj)
        db.session.commit()
