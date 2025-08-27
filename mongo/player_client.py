from typing import Optional
from datetime import datetime
from logger import log
from models import Player
from .base_client import BaseMongoClient

STATUS_AVAILABLE = "available"
STATUS_LOCKED = "locked"
STATUS_USED = "used"
STATUS_UNAVAILABLE = "unavailable"


class PlayerMongoClient(BaseMongoClient):
    COLLECTION_NAME = "players"

    def __init__(self, player: Player, **kwargs):
        super().__init__(**kwargs)
        self.collection = self.db[self.COLLECTION_NAME]
        self.player = player
        self._id: Optional[str] = None

    @property
    def id(self):
        return self.player.player_id

    def insert(self):
        try:
            player_data = self.player.__dict__
            result = self.collection.insert_one(player_data)
            self._id = result.inserted_id
            self.set_available()
            log.debug(f"Inserted player {self.player}")
        except Exception as e:
            log.exception(f"Error inserting player: {e}")
            return None

    def get(self, kind=None):
        try:
            if not self.id:
                raise ValueError("Cannot get player without valid ID")

            details = self.collection.find_one({"player_id": self.id})
            if kind:
                return details.get(kind)
            return details
        except Exception as e:
            log.error(f"Error retrieving player with ID: {self.id}")
            raise

    def update(self, **kwargs):
        try:
            if not self.id:
                raise ValueError("Cannot update player without valid ID")

            update_data = {k: v for k, v in kwargs.items() if v is not None}
            if not update_data:
                log.warning("No valid fields to update")
                return

            result = self.collection.update_one({"player_id": self.id}, {"$set": update_data})

            if result.modified_count > 0:
                log.debug(f"Player {self.id} updated successfully")
            else:
                log.warning(f"No player was updated for ID: {self._id}")
        except Exception as e:
            log.error(f"Failed to update player {self._id}: {e}")
            raise

    def lock(self):
        self.update(status=STATUS_LOCKED, locked_at=datetime.utcnow())

    def set_available(self):
        self.update(status=STATUS_AVAILABLE, locked_at=None)

    def set_used(self):
        self.update(status=STATUS_USED, locked_at=None)

    def set_unavailable(self):
        self.update(status=STATUS_UNAVAILABLE, locked_at=None)

    def set_registered(self):
        self.update(status=STATUS_AVAILABLE, registration_date=datetime.utcnow(), is_verified=False)

    def set_verified(self):
        self.update(status=STATUS_AVAILABLE, is_verified=True, verification_date=datetime.utcnow())

    def delete(self):
        try:
            if not self.id:
                raise ValueError("Cannot delete player without valid ID")

            result = self.collection.delete_one({"player_id": self.id})

            if result.deleted_count > 0:
                log.debug(f"Successfully deleted player {self._id}")
                self._id = None
            else:
                log.warning(f"No player was deleted for ID: {self._id}")

        except Exception as e:
            log.error(f"Failed to delete player {self._id}: {e}")
            raise

