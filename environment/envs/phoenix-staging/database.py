"""
Phoenix Staging Environment Database Configuration
"""

# PostgreSQL Configuration
host = "phoenix-staging-db.example.com"
port = 5432
database = "phoenix_staging_db"
username = "phoenix_staging_user"
password = "phoenix_staging_password"

# Connection Pool Configuration
min_connections = 1
max_connections = 20
connection_timeout = 30

# Query Configuration
query_timeout = 60
autocommit = False
