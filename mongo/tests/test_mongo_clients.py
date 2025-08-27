from unittest.mock import MagicMock, patch
from mongo.base_client import BaseMongoClient
from mongo.player_client import PlayerClient
from mongo.operator_client import OperatorClient


class TestMongoClients:

    @patch("mongo.base_client.MongoClient")
    def test_base_client_initialization(self, mock_mongo_client):
        mock_client = MagicMock()
        mock_db = MagicMock()
        mock_client.__getitem__.return_value = mock_db
        mock_mongo_client.return_value = mock_client

        with patch("mongo.base_client.logger"):
            client = BaseMongoClient(host="localhost", port=27017, database="test_db")
            assert client.host == "localhost"
            assert client.port == 27017
            assert client.database == "test_db"
            mock_mongo_client.assert_called_once()

    @patch("mongo.base_client.MongoClient")
    def test_base_client_context_manager(self, mock_mongo_client):
        mock_client = MagicMock()
        mock_db = MagicMock()
        mock_client.__getitem__.return_value = mock_db
        mock_mongo_client.return_value = mock_client

        with patch("mongo.base_client.logger"):
            with BaseMongoClient(host="localhost", port=27017, database="test_db") as client:
                assert client is not None
            mock_client.close.assert_called_once()

    @patch("mongo.player_client.BaseMongoClient")
    def test_player_client_initialization(self, mock_base_client):
        mock_db = MagicMock()
        mock_collection = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_base_client.return_value.db = mock_db

        player_data = {"_id": "test_id", "name": "Test Player"}

        with patch("mongo.player_client.logger"):
            client = PlayerClient(player_data)
            assert client._id == "test_id"
            assert client._player_data == player_data

    @patch("mongo.player_client.BaseMongoClient")
    def test_player_get_available_player(self, mock_base_client):
        mock_db = MagicMock()
        mock_collection = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_base_client.return_value.db = mock_db

        player_data = {"_id": "test_id", "name": "Test Player"}
        mock_collection.find_one_and_update.return_value = player_data

        with patch("mongo.player_client.logger"):
            result = PlayerClient.get_available_player({"is_verified": True})
            assert result is not None
            assert result._id == "test_id"

    @patch("mongo.player_client.BaseMongoClient")
    def test_player_update_operations(self, mock_base_client):
        mock_db = MagicMock()
        mock_collection = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_base_client.return_value.db = mock_db

        player_data = {"_id": "test_id", "name": "Test Player"}
        mock_collection.update_one.return_value.modified_count = 1

        with patch("mongo.player_client.logger"):
            client = PlayerClient(player_data)
            client.collection = mock_collection
            client.update_player({"last_login": "2024-07-15"})
            mock_collection.update_one.assert_called_once()

    @patch("mongo.operator_client.BaseMongoClient")
    def test_operator_client_initialization(self, mock_base_client):
        mock_db = MagicMock()
        mock_collection = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_base_client.return_value.db = mock_db

        operator_data = {"_id": "test_id", "username": "admin"}

        with patch("mongo.operator_client.logger"):
            client = OperatorClient(operator_data)
            assert client._id == "test_id"
            assert client._operator_data == operator_data

    @patch("mongo.operator_client.BaseMongoClient")
    def test_operator_get_available_operator(self, mock_base_client):
        mock_db = MagicMock()
        mock_collection = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_base_client.return_value.db = mock_db

        operator_data = {"_id": "test_id", "username": "admin"}
        mock_collection.find_one_and_update.return_value = operator_data

        with patch("mongo.operator_client.logger"):
            result = OperatorClient.get_available_operator({"role": "admin"})
            assert result is not None
            assert result._id == "test_id"

    @patch("mongo.operator_client.BaseMongoClient")
    def test_operator_update_operations(self, mock_base_client):
        mock_db = MagicMock()
        mock_collection = MagicMock()
        mock_db.__getitem__.return_value = mock_collection
        mock_base_client.return_value.db = mock_db

        operator_data = {"_id": "test_id", "username": "admin"}
        mock_collection.update_one.return_value.modified_count = 1

        with patch("mongo.operator_client.logger"):
            client = OperatorClient(operator_data)
            client.collection = mock_collection
            client.update_operator({"last_login": "2024-07-15"})
            mock_collection.update_one.assert_called_once()

    def test_player_unlock_functionality(self):
        with patch("mongo.player_client.BaseMongoClient") as mock_base_client:
            mock_db = MagicMock()
            mock_collection = MagicMock()
            mock_db.__getitem__.return_value = mock_collection
            mock_base_client.return_value.db = mock_db

            player_data = {"_id": "test_id", "status": "LOCKED"}
            mock_collection.update_one.return_value.modified_count = 1

            with patch("mongo.player_client.logger"):
                client = PlayerClient(player_data)
                client.collection = mock_collection
                client.unlock_player()
                mock_collection.update_one.assert_called_once()

    def test_operator_unlock_functionality(self):
        with patch("mongo.operator_client.BaseMongoClient") as mock_base_client:
            mock_db = MagicMock()
            mock_collection = MagicMock()
            mock_db.__getitem__.return_value = mock_collection
            mock_base_client.return_value.db = mock_db

            operator_data = {"_id": "test_id", "status": "LOCKED"}
            mock_collection.update_one.return_value.modified_count = 1

            with patch("mongo.operator_client.logger"):
                client = OperatorClient(operator_data)
                client.collection = mock_collection
                client.unlock_operator()
                mock_collection.update_one.assert_called_once()

    def test_player_properties(self):
        with patch("mongo.player_client.BaseMongoClient"):
            player_data = {"_id": "test_id", "status": "LOCKED"}

            with patch("mongo.player_client.logger"):
                client = PlayerClient(player_data)
                assert client.player_id == "test_id"
                assert client.is_locked is True

    def test_operator_properties(self):
        with patch("mongo.operator_client.BaseMongoClient"):
            operator_data = {"_id": "test_id", "status": "LOCKED"}

            with patch("mongo.operator_client.logger"):
                client = OperatorClient(operator_data)
                assert client.operator_id == "test_id"
                assert client.is_locked is True
