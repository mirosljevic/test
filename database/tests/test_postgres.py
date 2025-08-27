from database.postgres import PostgresClient
import pytest
from unittest.mock import MagicMock, patch


class TestPostgresClient:

    @patch("database.postgres.ThreadedConnectionPool")
    @patch("database.postgres.psycopg2")
    def test_init_with_connection_pool(self, mock_psycopg2, mock_pool):
        with patch("database.postgres.logger"):
            client = PostgresClient(host="localhost", port=5432, database="test_db",
                                    username="test_user", password="test_pass",
                                    use_connection_pool=True)
            assert client.use_connection_pool is True
            mock_pool.assert_called_once()

    @patch("database.postgres.psycopg2")
    def test_init_without_connection_pool(self, mock_psycopg2):
        mock_connection = MagicMock()
        mock_psycopg2.connect.return_value = mock_connection

        with patch("database.postgres.logger"):
            client = PostgresClient(host="localhost", port=5432, database="test_db",
                                    username="test_user", password="test_pass",
                                    use_connection_pool=False)
            assert client.use_connection_pool is False

    @patch("database.postgres.psycopg2")
    def test_execute_query_with_fetch(self, mock_psycopg2):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_row = {"id": 1, "name": "test"}
        mock_cursor.fetchall.return_value = [mock_row]
        mock_connection.cursor.return_value = mock_cursor
        mock_psycopg2.connect.return_value = mock_connection

        with patch("database.postgres.logger"):
            client = PostgresClient(host="localhost", port=5432, database="test_db",
                                    username="test_user", password="test_pass",
                                    use_connection_pool=False)
            result = client.execute_query("SELECT * FROM users", fetch=True)

            assert result == [mock_row]
            mock_cursor.execute.assert_called()

    @patch("database.postgres.psycopg2")
    def test_select_operation(self, mock_psycopg2):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_row = {"id": 1, "name": "test"}
        mock_cursor.fetchall.return_value = [mock_row]
        mock_connection.cursor.return_value = mock_cursor
        mock_psycopg2.connect.return_value = mock_connection

        with patch("database.postgres.logger"):
            client = PostgresClient(host="localhost", port=5432, database="test_db",
                                    username="test_user", password="test_pass",
                                    use_connection_pool=False)
            result = client.select("users", where="id = %s", params=(1,))

            assert result == [mock_row]

    @patch("database.postgres.psycopg2")
    def test_insert_operation(self, mock_psycopg2):
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        mock_psycopg2.connect.return_value = mock_connection

        with patch("database.postgres.logger"):
            client = PostgresClient(host="localhost", port=5432, database="test_db",
                                    username="test_user", password="test_pass",
                                    use_connection_pool=False)
            client.insert("users", {"name": "test", "email": "test@example.com"})

            mock_cursor.execute.assert_called()

    @patch("database.postgres.psycopg2")
    def test_context_manager(self, mock_psycopg2):
        mock_connection = MagicMock()
        mock_psycopg2.connect.return_value = mock_connection

        with patch("database.postgres.logger"):
            with PostgresClient(host="localhost", port=5432, database="test_db",
                                username="test_user", password="test_pass",
                                use_connection_pool=False) as client:
                assert client is not None
            mock_connection.close.assert_called()

    @patch("database.postgres.psycopg2")
    def test_update_empty_data(self, mock_psycopg2):
        """Test UPDATE with empty data."""
        client = PostgresClient(use_connection_pool=False)

        with pytest.raises(ValueError, match="Update data cannot be empty"):
            client.update("users", {}, "id = %s", (1,))

    @patch("database.postgres.psycopg2")
    def test_update_no_where_clause(self, mock_psycopg2):
        """Test UPDATE without WHERE clause."""
        client = PostgresClient(use_connection_pool=False)

        with pytest.raises(
            ValueError, match="WHERE clause is required for UPDATE operations"
        ):
            client.update("users", {"name": "Test"}, "")

    @patch("database.postgres.PostgresClient.execute_query")
    @patch("database.postgres.psycopg2")
    def test_delete(self, mock_psycopg2, mock_execute):
        """Test DELETE operation."""
        client = PostgresClient(use_connection_pool=False)

        client.delete("users", "id = %s", (1,))

        expected_query = "DELETE FROM users WHERE id = %s"
        mock_execute.assert_called_once_with(expected_query, (1,))

    @patch("database.postgres.psycopg2")
    def test_delete_no_where_clause(self, mock_psycopg2):
        """Test DELETE without WHERE clause."""
        client = PostgresClient(use_connection_pool=False)

        with pytest.raises(
            ValueError, match="WHERE clause is required for DELETE operations"
        ):
            client.delete("users", "")

    @patch("database.postgres.ThreadedConnectionPool")
    @patch("database.postgres.psycopg2")
    def test_close_connection_pool(self, mock_psycopg2, mock_pool_class):
        """Test closing connection pool."""
        mock_pool = MagicMock()
        mock_pool_class.return_value = mock_pool

        client = PostgresClient(use_connection_pool=True)
        client.close()

        mock_pool.closeall.assert_called_once()

    @patch("database.postgres.psycopg2")
    def test_close_single_connection(self, mock_psycopg2):
        """Test closing single connection."""
        mock_connection = MagicMock()
        mock_psycopg2.connect.return_value = mock_connection

        client = PostgresClient(use_connection_pool=False)
        client.close()

        mock_connection.close.assert_called_once()
