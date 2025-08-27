from pymongo import MongoClient
from pymongo.database import Database
from typing import Optional

from logger import log
from settings.environment import ENVIRONMENT
from settings.mongo import (MONGO_HOST, MONGO_PORT, MONGO_USER, MONGO_PASSWORD,
                           MONGO_CONNECTION_TIMEOUT, MONGO_SOCKET_TIMEOUT, MONGO_MAX_IDLE_TIME,
                           MONGO_SERVER_SELECTION_TIMEOUT, MONGO_MAX_POOL_SIZE, MONGO_MIN_POOL_SIZE)


class BaseMongoClient:
    def __init__(self, **kwargs):
        self.host = MONGO_HOST
        self.port = MONGO_PORT
        self.database = ENVIRONMENT
        self.username = MONGO_USER
        self.password = MONGO_PASSWORD

        self.connection_timeout_ms = MONGO_CONNECTION_TIMEOUT
        self.socket_timeout_ms = MONGO_SOCKET_TIMEOUT
        self.server_selection_timeout_ms = MONGO_SERVER_SELECTION_TIMEOUT
        self.max_pool_size = MONGO_MAX_POOL_SIZE
        self.min_pool_size = MONGO_MIN_POOL_SIZE
        self.max_idle_time_ms = MONGO_MAX_IDLE_TIME

        self.client: Optional[MongoClient] = None
        self.db: Optional[Database] = None

        self._connect()

    def _connect(self):
        try:
            if self.username and self.password:
                auth_string = f"{self.username}:{self.password}@"
            else:
                auth_string = ""

            uri = f"mongodb://{auth_string}{self.host}:{self.port}/{self.database}?authSource=admin"

            connection_options = {
                "connectTimeoutMS": self.connection_timeout_ms,
                "socketTimeoutMS": self.socket_timeout_ms,
                "serverSelectionTimeoutMS": self.server_selection_timeout_ms,
                "maxPoolSize": self.max_pool_size,
                "minPoolSize": self.min_pool_size,
                "maxIdleTimeMS": self.max_idle_time_ms,
            }

            self.client = MongoClient(uri, **connection_options)
            self.db = self.client[self.database]
            self.client.admin.command("ping")
            log.debug(f"Connected to MongoDB database: {self.database}")

        except Exception as e:
            log.exception(f"Failed to connect to MongoDB: {e}")
            raise

    def close(self):
        if self.client:
            try:
                self.client.close()
                log.debug("MongoDB connection closed")
            except Exception as e:
                log.exception(f"Error closing MongoDB connection: {e}")
            finally:
                self.client = None
                self.db = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
