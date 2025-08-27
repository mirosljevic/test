# Database Framework 🗄️

PostgreSQL database framework with connection management, query utilities, data validation, and comprehensive testing support.

## Overview

The database framework provides robust PostgreSQL integration with connection pooling, transaction management, data validation, and seamless integration with the test automation framework.

## Key Features

- **PostgreSQL Integration**: Native PostgreSQL support with psycopg2
- **Connection Management**: Connection pooling and lifecycle management
- **Query Utilities**: Helper methods for common database operations
- **Data Validation**: Result validation and schema checking
- **Transaction Support**: Transaction management with rollback capabilities
- **Multi-Environment**: Support for different database environments

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Configure database settings in your environment package:

```python
# environment/envs/{env}/database.py
host = "localhost"
port = 5432
database = "test_db"
username = "test_user"
password = "test_password"

# Optional settings
min_connections = 1
max_connections = 20
connection_timeout = 30
query_timeout = 60
autocommit = False
```

## Usage

### Basic Usage

```python
from database import PostgresClient

# Using connection pool (recommended)
with PostgresClient() as db:
    users = db.select("users")
    print(f"Found {len(users)} users")
```

### CRUD Operations

```python
from database import PostgresClient

with PostgresClient() as db:
    # Insert
    db.insert("users", {"name": "John", "email": "john@example.com"})
    
    # Select
    users = db.select("users", where="active = %s", params=(True,))
    
    # Update
    db.update("users", {"name": "John Updated"}, 
              where="email = %s", where_params=("john@example.com",))
    
    # Delete
    db.delete("users", where="email = %s", params=("john@example.com",))
```

### SQL File Execution

```python
from database import PostgresClient

with PostgresClient() as db:
    # Execute SQL from file
    results = db.execute_query_from_file("queries/users.sql", 
                                        params=(True,), fetch=True)
    
    # Execute complex operations
    db.execute_query_from_file("migrations/001_create_tables.sql")
```

### Raw SQL Queries

```python
from database import PostgresClient

with PostgresClient() as db:
    # Execute with results
    results = db.execute_query("SELECT * FROM users WHERE id = %s", 
                              params=(1,), fetch=True)
    
    # Execute without results
    db.execute_query("UPDATE users SET active = %s WHERE id = %s", 
                     params=(True, 1))
```

## Connection Modes

### Connection Pool (Default)
```python
# Best for concurrent operations
client = PostgresClient(use_connection_pool=True)
```

### Single Connection
```python
# Best for sequential operations
client = PostgresClient(use_connection_pool=False)
```

## Error Handling

The package provides comprehensive error handling:

```python
from database import PostgresClient

try:
    with PostgresClient() as db:
        db.execute_query("INVALID SQL")
except Exception as e:
    print(f"Database error: {e}")
```

## Testing

Run the test suite:

```bash
python -m pytest database/tests/
```

## Dependencies

- `psycopg2`: PostgreSQL adapter
- `environment`: Environment configuration
- `logger`: Logging utilities

## Package Structure

```
database/
├── __init__.py          # Package exports
├── postgres.py          # PostgreSQL client implementation
├── requirements.txt     # Package dependencies
├── samples/            # Usage examples
│   ├── basic_operations.py
│   └── sql_file_execution.py
└── tests/              # Test suite
    └── test_postgres.py
```

## Best Practices

1. **Use Context Managers**: Always use `with` statements for automatic cleanup
2. **Connection Pooling**: Use connection pools for concurrent operations
3. **Parameterized Queries**: Always use parameters to prevent SQL injection
4. **Error Handling**: Wrap database operations in try-catch blocks
5. **File Organization**: Store SQL files in dedicated directories

## Environment Examples

### Development
```python
host = "localhost"
port = 5432
database = "test_dev"
username = "dev_user"
password = "dev_password"
```

### Production
```python
host = "prod-db.example.com"
port = 5432
database = "production_db"
username = "prod_user"
password = "secure_password"
max_connections = 50
```

## Common Use Cases

### Test Data Management
```python
def setup_test_data():
    with PostgresClient() as db:
        db.execute_query("TRUNCATE users RESTART IDENTITY CASCADE")
        db.insert("users", {"name": "Test User", "email": "test@example.com"})
```

### Data Validation
```python
def validate_user_exists(email):
    with PostgresClient() as db:
        users = db.select("users", where="email = %s", params=(email,))
        return len(users) > 0
```

### Batch Operations
```python
def batch_insert_users(user_list):
    with PostgresClient() as db:
        for user in user_list:
            db.insert("users", user)
```

## Basic Usage

### Simple Database Operations

```python
from database import PostgresClient

# Using context manager (recommended)
with PostgresClient() as db:
    # Insert data
    db.insert('users', {
        'name': 'John Doe', 
        'email': 'john@example.com'
    })
    
    # Select data
    users = db.select('users', where='active = %s', params=(True,))
    
    # Update data
    db.update('users', 
              {'last_login': 'NOW()'}, 
              'email = %s', 
              ('john@example.com',))
    
    # Delete data
    db.delete('users', 'id = %s', (user_id,))
```

### Connection Pool vs Single Connection

```python
# With connection pool (default, recommended for concurrent operations)
with PostgresClient(use_connection_pool=True) as db:
    # Multiple operations can use different connections from pool
    pass

# With single connection (better for transactions)
with PostgresClient(use_connection_pool=False) as db:
    # All operations use the same connection
    pass
```

### Executing Raw SQL

```python
with PostgresClient() as db:
    # Execute query without results
    db.execute_query("CREATE INDEX idx_user_email ON users(email)")
    
    # Execute query with results
    results = db.execute_query(
        "SELECT * FROM users WHERE created_at > %s", 
        (datetime.now() - timedelta(days=7),),
        fetch=True
    )
    
    # Execute query from file
    results = db.execute_query_from_file(
        "complex_analytics.sql", 
        params=(start_date, end_date),
        fetch=True
    )
```

### CRUD Operations

#### SELECT Operations

```python
with PostgresClient() as db:
    # Select all columns
    all_users = db.select('users')
    
    # Select specific columns
    names = db.select('users', 'name, email')
    
    # Select with WHERE clause
    active_users = db.select('users', 
                            where='active = %s AND created_at > %s', 
                            params=(True, last_week))
    
    # Complex select with joins (use execute_query for complex queries)
    results = db.execute_query("""
        SELECT u.name, p.title, p.created_at
        FROM users u
        JOIN posts p ON u.id = p.user_id
        WHERE u.active = %s
        ORDER BY p.created_at DESC
        LIMIT %s
    """, (True, 10), fetch=True)
```

#### INSERT Operations

```python
with PostgresClient() as db:
    # Single insert
    db.insert('users', {
        'name': 'Jane Smith',
        'email': 'jane@example.com',
        'active': True
    })
    
    # Multiple inserts
    users_data = [
        {'name': 'User 1', 'email': 'user1@example.com'},
        {'name': 'User 2', 'email': 'user2@example.com'},
        {'name': 'User 3', 'email': 'user3@example.com'}
    ]
    
    for user_data in users_data:
        db.insert('users', user_data)
```

#### UPDATE Operations

```python
with PostgresClient() as db:
    # Simple update
    db.update('users', 
              {'last_login': 'NOW()', 'login_count': 'login_count + 1'}, 
              'email = %s', 
              ('user@example.com',))
    
    # Update multiple records
    db.update('users', 
              {'status': 'inactive'}, 
              'last_login < %s', 
              (cutoff_date,))
```

#### DELETE Operations

```python
with PostgresClient() as db:
    # Delete specific record
    db.delete('users', 'id = %s', (user_id,))
    
    # Delete multiple records
    db.delete('logs', 'created_at < %s', (cutoff_date,))
    
    # Note: WHERE clause is required for safety
```

### Transaction Management

```python
with PostgresClient(use_connection_pool=False) as db:
    try:
        # Start transaction
        db.execute_query("BEGIN")
        
        # Multiple operations
        db.update('accounts', {'balance': 'balance - %s'}, 'id = %s', (amount, from_account))
        db.update('accounts', {'balance': 'balance + %s'}, 'id = %s', (amount, to_account))
        
        # Insert transaction log
        db.insert('transactions', {
            'from_account': from_account,
            'to_account': to_account,
            'amount': amount,
            'type': 'transfer'
        })
        
        # Commit transaction
        db.execute_query("COMMIT")
        
    except Exception as e:
        # Rollback on error
        db.execute_query("ROLLBACK")
        raise
```

### SQL File Execution

Create SQL files and execute them:

```sql
-- queries/create_user_table.sql
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```python
with PostgresClient() as db:
    # Execute schema creation
    db.execute_query_from_file('queries/create_user_table.sql')
    
    # Execute complex query with parameters
    results = db.execute_query_from_file(
        'queries/user_analytics.sql',
        params=(start_date, end_date),
        fetch=True
    )
```

## Error Handling

The package provides comprehensive error handling:

```python
from database import PostgresClient

with PostgresClient() as db:
    try:
        # Database operations
        db.insert('users', {'invalid': 'data'})
    except psycopg2.IntegrityError as e:
        # Handle constraint violations
        logger.error(f"Data integrity error: {e}")
    except psycopg2.OperationalError as e:
        # Handle connection/operational errors
        logger.error(f"Database operation error: {e}")
    except FileNotFoundError as e:
        # Handle missing SQL files
        logger.error(f"SQL file not found: {e}")
    except ValueError as e:
        # Handle validation errors (empty data, missing WHERE clause, etc.)
        logger.error(f"Validation error: {e}")
    except Exception as e:
        # Handle other errors
        logger.error(f"Unexpected error: {e}")
```

## Testing

Run the test suite:

```bash
# Run all tests
pytest database/tests/

# Run with coverage
pytest database/tests/ --cov=database

# Run specific test file
pytest database/tests/test_postgres.py

# Run with verbose output
pytest database/tests/ -v
```

## Examples

The `samples/` directory contains comprehensive examples:

- `basic_operations.py`: Basic CRUD operations
- `sql_file_execution.py`: Executing SQL from files
- `transaction_management.py`: Transaction handling and error management

Run examples:

```bash
python database/samples/basic_operations.py
python database/samples/sql_file_execution.py
python database/samples/transaction_management.py
```

## Configuration Options

All configuration is loaded from the environment package. Available options:

| Option | Description | Default |
|--------|-------------|---------|
| `host` | Database hostname | Required |
| `port` | Database port | 5432 |
| `database` | Database name | Required |
| `username` | Database username | Required |
| `password` | Database password | Required |
| `min_connections` | Minimum pool connections | 1 |
| `max_connections` | Maximum pool connections | 20 |
| `connection_timeout` | Connection timeout (seconds) | 30 |
| `query_timeout` | Query timeout (seconds) | 60 |
| `autocommit` | Auto-commit mode | False |

## Best Practices

1. **Use Context Managers**: Always use `with` statements for automatic cleanup
2. **Connection Pooling**: Use connection pools for concurrent operations
3. **Single Connections**: Use single connections for transactions
4. **Parameter Binding**: Always use parameter binding to prevent SQL injection
5. **Error Handling**: Implement proper error handling for database operations
6. **WHERE Clauses**: Always include WHERE clauses for UPDATE and DELETE operations
7. **Transactions**: Use transactions for multi-step operations
8. **Logging**: Enable debug logging to monitor database operations

## Logging

The package integrates with the logger package and provides debug-level logging:

```python
# Enable debug logging to see all database operations
import logging
logging.getLogger().setLevel(logging.DEBUG)
```

Debug logs include:
- Connection pool creation/destruction
- Query execution with parameters
- Transaction operations
- Error details

## Dependencies

- `psycopg2-binary>=2.9.0`: PostgreSQL adapter for Python
- `environment`: Environment configuration package
- `logger`: Logging package

## Architecture

The package follows these design principles:

- **Single Responsibility**: Each class has a focused purpose
- **Environment Integration**: Seamless configuration from environment package
- **Resource Management**: Proper connection and cursor cleanup
- **Error Resilience**: Comprehensive error handling and recovery
- **Performance**: Connection pooling for optimal performance
- **Type Safety**: Full type hints for IDE support
- **Testability**: Comprehensive test coverage with mocking

## License

This package is part of the test automation framework and follows the same licensing terms.
