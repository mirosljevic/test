"""
Phoenix Staging Environment Settings Configuration
"""

# Feature toggles
enable_new_ui = True
enable_beta_features = True
enable_debug_mode = True
enable_analytics = False

# Timeouts and limits
api_timeout = 30
request_timeout = 15
max_retries = 3
rate_limit_per_minute = 1000

# Security settings
jwt_expiry_hours = 24
session_timeout_minutes = 60
max_login_attempts = 5

# Game configuration
min_bet_amount = 1.0
max_bet_amount = 1000.0
default_game_timeout = 300

# Notification settings
email_notifications_enabled = True
sms_notifications_enabled = False
push_notifications_enabled = True

# Tenant configuration
tenant = "Kansas"

# Cache settings
cache_ttl_seconds = 3600
enable_redis_cache = True

# Environment specific flags
is_production = False
maintenance_mode = False
log_level = "DEBUG"
