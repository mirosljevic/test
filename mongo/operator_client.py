from typing import Dict, Any, Optional, List
from datetime import datetime
from logger import log
from models import Operator, OperatorRole
from .base_client import BaseMongoClient

STATUS_AVAILABLE = "available"
STATUS_LOCKED = "locked"
STATUS_UNAVAILABLE = "unavailable"


class OperatorMongoClient(BaseMongoClient):
    COLLECTION_NAME = "operators"

    def __init__(self, operator: Operator, mongo_id=None, **kwargs):
        super().__init__(**kwargs)
        self.collection = self.db[self.COLLECTION_NAME]
        self.operator = operator
        self._id = mongo_id

    @property
    def user(self) -> str:
        return self.operator.username

    def insert(self):
        try:
            operator_data = self.operator.__dict__
            result = self.collection.insert_one(operator_data)
            self._id = result.inserted_id
            self.set_available()
            log.debug(f"Inserted operator with ID: {self._id}")
        except Exception as e:
            log.exception(f"Error inserting operator: {e}")
            raise

    def get(self):
        try:
            if not self.user:
                log.exception("Operator Username is not set. Cannot retrieve operator.")
                raise
            return self.collection.find_one({"username": self.user})
        except Exception as e:
            log.error(f"Error retrieving operator: {e}")
            raise

    def update(self, **kwargs):
        try:
            if not self.user:
                log.exception("Operator username is not set. Cannot update operator.")
                raise

            update_data = {k: v for k, v in kwargs.items() if v is not None}
            if update_data:
                result = self.collection.update_one({"username": self.user}, {"$set": update_data})
                if result.modified_count > 0:
                    log.debug(f"Updated operator with ID: {self.user} {kwargs}")
                else:
                    log.debug(f"No changes made to operator with ID: {self.user}")
            else:
                log.debug("No update data provided.")
        except Exception as e:
            log.error(f"Error updating operator: {e}")
            raise

    def set_available(self):
        self.update(status=STATUS_AVAILABLE, last_active=datetime.utcnow())
        log.debug(f"Operator {self.user} set to available at {datetime.utcnow()}")

    def lock(self):
        self.update(status=STATUS_LOCKED, locked_at=datetime.utcnow())
        log.debug(f"Operator {self.user} locked at {datetime.utcnow()}")

    def set_unavailable(self):
        self.update(status=STATUS_UNAVAILABLE)
        log.debug(f"Operator {self.user} set to unavailable at {datetime.utcnow()}")

    def delete(self):
        try:
            if not self._id:
                log.exception("Operator ID is not set. Cannot delete operator.")
                raise

            result = self.collection.delete_one({"username": self.user})
            if result.deleted_count > 0:
                log.debug(f"Deleted operator with ID: {self.user}")
            else:
                log.debug(f"No operator found with ID: {self.user} to delete")
        except Exception as e:
            log.error(f"Error deleting operator: {e}")
            raise
