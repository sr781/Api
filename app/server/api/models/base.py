from app.database import db
from sqlalchemy.exc import IntegrityError, OperationalError
import time


class DBInterface:
    """Interface class to handle common DB interaction methods (add, update, delete etc)."""

    def __init__(self, cursor, model):
        self.cursor = cursor
        self.model = model

    def add_to_db(self):
        """
        Add object to DB.
        TODO: TEST OPERATIONAL FAILURE
        """
        num_retries = 5
        db_insertion_success = False

        while num_retries > 0:
            try:
                self.cursor.add(self.model)
                self._commit()
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
    def get_object(model, **kwargs):
        try:
            obj = model.query.filter_by(**kwargs).first()
            if obj:
                return obj
            else:
                return None
        except (IntegrityError, OperationalError):
            return None

    def update_object(self, attrs):
        """Update object details"""
        try:
            for key, value in attrs.items():
                if not hasattr(self.model, key):
                    raise ValueError
                else:
                    setattr(self.model, key, value)
            self._commit()
            return True
        except (IntegrityError, OperationalError) as e:
            self.cursor.rollback()
            return e

    def remove_from_db(self):
        """Remove object from DB."""
        try:
            self.cursor.delete(self.model)
            self.cursor.commit()
            return True
        except (IntegrityError, OperationalError):
            self.cursor.rollback()
            return None

    def _commit(self):
        """Commit transaction."""
        self.cursor.commit()