import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool
from typing import List, Dict, Any, Optional, Union
from pathlib import Path
from environment import database

try:
    from logger import log as logger
except ImportError:
    import logging
    logger = logging.getLogger(__name__)


class PostgresClient:
    def __init__(self, use_connection_pool: bool = True, **kwargs):
        self.use_connection_pool = use_connection_pool
        self.connection_pool = None
        self.single_connection = None

        self.host = database.host
        self.port = database.port
        self.database = database.database
        self.username = database.user
        self.password = database.password

        self.min_connections = kwargs.get("min_connections", 1)
        self.max_connections = kwargs.get("max_connections", 20)
        self.connection_timeout = kwargs.get("connection_timeout", 30)
        self.query_timeout = kwargs.get("query_timeout", 60)
        self.autocommit = kwargs.get("autocommit", False)

        logger.debug(
            f"Initializing PostgresClient for {self.host}:{self.port}/{self.database}"
        )

        if self.use_connection_pool:
            self._create_connection_pool()
        else:
            self._create_single_connection()

    def _create_connection_pool(self):
        try:
            self.connection_pool = ThreadedConnectionPool(
                minconn=self.min_connections,
                maxconn=self.max_connections,
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password,
                connect_timeout=self.connection_timeout,
            )
            logger.debug(
                f"Created connection pool with {self.min_connections}-{self.max_connections} connections"
            )
        except Exception as e:
            logger.error(f"Failed to create connection pool: {e}")
            raise

    def _create_single_connection(self):
        try:
            self.single_connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password,
                connect_timeout=self.connection_timeout,
            )
            self.single_connection.autocommit = self.autocommit
            logger.debug("Created single database connection")
        except Exception as e:
            logger.error(f"Failed to create database connection: {e}")
            raise

    def get_connection(self):
        if self.use_connection_pool:
            return self.connection_pool.getconn()
        else:
            return self.single_connection

    def return_connection(self, connection):
        if self.use_connection_pool and connection:
            self.connection_pool.putconn(connection)

    def execute_query(
        self, query: str, params: Optional[tuple] = None, fetch: bool = False
    ) -> Optional[Union[List[Dict[str, Any]], int]]:
        connection = None
        cursor = None

        try:
            connection = self.get_connection()
            cursor = connection.cursor(cursor_factory=RealDictCursor)

            cursor.execute(
                f"SET statement_timeout = {self.query_timeout * 1000}")

            logger.debug(f"Executing query: {query}")
            if params:
                logger.debug(f"Query parameters: {params}")

            cursor.execute(query, params)

            if fetch:
                results = cursor.fetchall()
                logger.debug(f"Query returned {len(results)} rows")
                return [dict(row) for row in results]
            else:
                # Always commit for non-fetch operations unless autocommit is enabled
                if not self.autocommit:
                    connection.commit()
                rows_affected = cursor.rowcount
                logger.debug(f"Query executed successfully, {rows_affected} rows affected")
                return rows_affected

        except Exception as e:
            logger.error(f"Query execution failed: {e}")
            if connection and not self.autocommit:
                connection.rollback()
            raise
        finally:
            if cursor:
                cursor.close()
            if connection:
                self.return_connection(connection)

    def execute_query_from_file(
        self,
        file_path: Union[str, Path],
        params: Optional[tuple] = None,
        fetch: bool = False,
    ) -> Optional[Union[List[Dict[str, Any]], int]]:
        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"SQL file not found: {file_path}")

        logger.debug(f"Reading SQL query from file: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            query = f.read().strip()

        if not query:
            raise ValueError(f"SQL file is empty: {file_path}")

        return self.execute_query(query, params, fetch)

    def _is_sql_function(self, value: str) -> bool:
        """Check if a string value is a SQL function or expression."""
        return (
            value.startswith('nextval') or
            value.startswith('gen_random_uuid') or
            'NOW()' in value or
            'CURRENT_TIMESTAMP' in value or
            'CURRENT_DATE' in value or
            'CURRENT_TIME' in value or
            'INTERVAL' in value
        )

    def _build_where_clause(self, where: Union[str, Dict[str, Any]]) -> tuple:
        """Build WHERE clause and return (query_part, params)."""
        if isinstance(where, dict):
            where_conditions = []
            where_values = []
            for key, value in where.items():
                if value is None:
                    where_conditions.append(f"{key} IS NULL")
                else:
                    where_conditions.append(f"{key} = %s")
                    where_values.append(value)
            
            if where_conditions:
                where_clause = f" WHERE {' AND '.join(where_conditions)}"
                return where_clause, tuple(where_values)
            else:
                return "", tuple()
        else:
            # Handle string where clause
            return f" WHERE {where}", tuple()

    def select(
        self,
        table: str,
        columns: Union[str, List[str]] = "*",
        where: Union[str, Dict[str, Any]] = "",
        params: Optional[tuple] = None,
        order_by: Optional[str] = None,
    ) -> List[Dict[str, Any]]:
        logger.debug(f"Selecting from table {table} with columns {columns} and where {where}")
        
        # Handle columns parameter
        if isinstance(columns, list):
            columns_str = ', '.join(columns) if columns else '*'
        else:
            columns_str = columns
        
        query = f"SELECT {columns_str} FROM {table}"
        
        if where:
            if isinstance(where, dict):
                # Build WHERE clause from dictionary - show formatted query in logs
                where_conditions = []
                for key, value in where.items():
                    if value is None:
                        where_conditions.append(f"{key} IS NULL")
                    elif isinstance(value, str):
                        # Escape single quotes for display and use in query
                        escaped_value = value.replace("'", "''")
                        where_conditions.append(f"{key} = '{escaped_value}'")
                    else:
                        where_conditions.append(f"{key} = {value}")
                
                if where_conditions:
                    where_clause = ' AND '.join(where_conditions)
                    query += f" WHERE {where_clause}"
                    final_params = None  # No params needed since we build complete query
                else:
                    final_params = params
            else:
                # Handle string where clause
                query += f" WHERE {where}"
                final_params = params
        else:
            final_params = params
        
        # Add ORDER BY if specified
        if order_by:
            query += f" ORDER BY {order_by}"
        
        logger.debug(f"Executing query: {query}")
        
        try:
            result = self.execute_query(query, final_params, fetch=True) or []
            logger.debug(f"Result: {len(result)} rows returned")
            return result
        except Exception as e:
            logger.error(f"Error selecting from table {table}: {e}")
            raise

    def insert(self, table: str, data: Dict[str, Any]) -> None:
        if not data:
            raise ValueError("Insert data cannot be empty")

        columns = ', '.join(data.keys())
        values_list = []
        
        for value in data.values():
            if isinstance(value, str) and self._is_sql_function(value):
                # SQL functions and expressions - add directly without quotes
                values_list.append(value)
            elif isinstance(value, str):
                # Regular string values - add with quotes and escape single quotes
                escaped_value = value.replace("'", "''")
                values_list.append(f"'{escaped_value}'")
            elif value is None:
                # NULL values
                values_list.append('NULL')
            else:
                # Numbers and other types - convert to string
                values_list.append(str(value))

        values_str = ', '.join(values_list)
        query = f"INSERT INTO {table} ({columns}) VALUES ({values_str})"

        try:
            logger.debug(f"Executing query: {query}")
            rows_affected = self.execute_query(query, params=None)
            if rows_affected and rows_affected > 0:
                logger.debug(f"Successfully inserted {rows_affected} row(s) into {table}")
            else:
                logger.warning(f"Insert executed but no rows were affected in {table}")
                raise ValueError(f"Insert failed: no rows were inserted into {table}")
        except Exception as e:
            logger.error(f"Failed to insert row into {table}: {e}")
            raise

    def update(
        self,
        table: str,
        data: Dict[str, Any],
        where: Union[str, Dict[str, Any]],
        where_params: Optional[tuple] = None,
    ) -> None:
        if not data:
            raise ValueError("Update data cannot be empty")

        if not where:
            raise ValueError("WHERE clause is required for UPDATE operations")

        # Build SET clause with proper handling of SQL functions
        set_parts = []
        update_params = []
        
        for col, value in data.items():
            if isinstance(value, str) and self._is_sql_function(value):
                # SQL functions and expressions - add directly without quotes
                set_parts.append(f"{col} = {value}")
            elif isinstance(value, str):
                # Regular string values - use parameterized query
                set_parts.append(f"{col} = %s")
                update_params.append(value)
            elif value is None:
                # NULL values
                set_parts.append(f"{col} = NULL")
            else:
                # Numbers and other types - use parameterized query
                set_parts.append(f"{col} = %s")
                update_params.append(value)

        set_clause = ", ".join(set_parts)
        query = f"UPDATE {table} SET {set_clause}"
        
        # Build WHERE clause
        where_clause, where_values = self._build_where_clause(where)
        query += where_clause
        
        # Combine parameters
        if isinstance(where, str) and where_params:
            all_params = tuple(update_params) + where_params
        else:
            all_params = tuple(update_params) + where_values

        try:
            logger.debug(f"Executing query: {query}")
            if all_params:
                logger.debug(f"Query parameters: {all_params}")
            rows_affected = self.execute_query(query, all_params)
            logger.debug(f"Updated {rows_affected} row(s) in {table}")
        except Exception as e:
            logger.error(f"Failed to update rows in {table}: {e}")
            raise

    def delete(
            self,
            table: str,
            where: Union[str, Dict[str, Any]],
            params: Optional[tuple] = None) -> None:
        if not where:
            raise ValueError("WHERE clause is required for DELETE operations")

        logger.debug(f"Deleting from table {table} with where {where}")
        
        query = f"DELETE FROM {table}"
        
        if isinstance(where, dict):
            # Build WHERE clause from dictionary - show formatted query in logs
            where_conditions = []
            for key, value in where.items():
                if value is None:
                    where_conditions.append(f"{key} IS NULL")
                elif isinstance(value, str):
                    # Escape single quotes for display and use in query
                    escaped_value = value.replace("'", "''")
                    where_conditions.append(f"{key} = '{escaped_value}'")
                else:
                    where_conditions.append(f"{key} = {value}")
            
            if where_conditions:
                where_clause = ' AND '.join(where_conditions)
                query += f" WHERE {where_clause}"
                final_params = None  # No params needed since we build complete query
            else:
                final_params = params
        else:
            # Handle string where clause
            query += f" WHERE {where}"
            final_params = params
        
        logger.debug(f"Executing query: {query}")
        
        try:
            rows_affected = self.execute_query(query, final_params)
            logger.debug(f"Deleted successfully, {rows_affected} row(s) affected")
        except Exception as e:
            logger.error(f"Error deleting from table {table}: {e}")
            raise
        
    def next_sequence_value(self, sequence_name: str) -> int:
        query = f"SELECT nextval('{sequence_name}')"
        result = self.execute_query(query, fetch=True)
        
        if result and len(result) == 1:
            return result[0]['nextval']
        else:
            raise ValueError(f"Failed to get next sequence value for {sequence_name}")

    def close(self):
        try:
            if self.connection_pool:
                self.connection_pool.closeall()
                logger.debug("Closed connection pool")
            elif self.single_connection:
                self.single_connection.close()
                logger.debug("Closed single connection")
        except Exception as e:
            logger.error(f"Error closing database connections: {e}")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
