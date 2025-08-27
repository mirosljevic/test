# Environment Configuration Framework ⚙️

Advanced environment management system with multi-tenant support, secure configuration loading, and dynamic environment switching.

## Overview

The environment framework provides robust configuration management with support for multiple environments, secure credential handling, and dynamic configuration loading for comprehensive test automation scenarios.

## Key Features

- **Multi-Environment Support**: Development, staging, production configurations
- **Secure Credential Management**: Encrypted credential storage and loading
- **Dynamic Configuration**: Runtime environment switching
- **Tenant Configuration**: Multi-tenant environment management
- **Environment Validation**: Configuration validation and health checks
- **Hot Reload**: Dynamic configuration updates without restart

## 📁 Structure

```
environment/
├── __init__.py              # Package exports
├── config.py               # Environment detection and selection
├── loader.py               # Dynamic module loading logic
├── envs/                   # Environment-specific configurations
│   ├── phoenix-staging/
│   │   ├── hosts.py       # Host URLs and endpoints
│   │   └── settings.py    # Feature toggles, timeouts, etc.
│   └── ks-staging/
│       ├── hosts.py       # Host URLs and endpoints
│       └── settings.py    # Feature toggles, timeouts, etc.
├── samples/
│   └── print_host.py      # Usage example
└── tests/
    └── test_loader.py     # Comprehensive test suite
```

## 🚀 Quick Start

### Basic Usage

```python
from environment import hosts, settings

# Access host configurations
print(f"Game Web URL: {hosts.game_web}")
print(f"Backoffice URL: {hosts.backoffice_url}")
print(f"Payment Gateway: {hosts.payment_gateway}")

# Access settings
print(f"API Timeout: {settings.api_timeout} seconds")
print(f"Debug Mode: {settings.enable_debug_mode}")
print(f"Max Bet Amount: ${settings.max_bet_amount}")
```

### Environment Selection

The active environment is determined by the `ENVIRONMENT` environment variable:

```bash
# Use phoenix-staging environment (default)
export ENVIRONMENT=phoenix-staging
python your_app.py

# Use ks-staging environment
export ENVIRONMENT=ks-staging
python your_app.py
```

If no `ENVIRONMENT` variable is set, it defaults to `"phoenix-staging"`.

## 🏗️ Adding New Environments

To add a new environment (e.g., `production`):

1. **Create the environment folder:**
   ```bash
   mkdir environment/envs/production
   ```

2. **Create the hosts configuration:**
   ```python
   # environment/envs/production/hosts.py
   """
   Production Environment Hosts Configuration
   """
   
   game_web = "https://game.example.com"
   game_api = "https://api.example.com"
   backoffice_url = "https://backoffice.example.com"
   admin_api = "https://admin.example.com"
   database_host = "production-db.example.com"
   # ... more hosts
   ```

3. **Create the settings configuration:**
   ```python
   # environment/envs/production/settings.py
   """
   Production Environment Settings Configuration
   """
   
   enable_debug_mode = False
   api_timeout = 60
   max_retries = 5
   is_production = True
   log_level = "WARNING"
   # ... more settings
   ```

4. **Use the new environment:**
   ```bash
   export ENVIRONMENT=production
   python your_app.py
   ```

The package will automatically load the new configuration with no code changes required!

## 📊 Configuration Examples

### Host Configuration (hosts.py)

```python
"""
Environment Hosts Configuration
"""

# Game and web services
game_web = "https://staging-game.example.com"
game_api = "https://staging-api.example.com"

# Backoffice and admin services
backoffice_url = "https://staging-backoffice.example.com"
admin_api = "https://staging-admin.example.com"

# Database and infrastructure
database_host = "staging-db.example.com"
redis_host = "staging-redis.example.com"

# External integrations
payment_gateway = "https://staging-payments.example.com"
notification_service = "https://staging-notifications.example.com"
```

### Settings Configuration (settings.py)

```python
"""
Environment Settings Configuration
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

# Environment specific flags
is_production = False
maintenance_mode = False
log_level = "DEBUG"
```

## 🧪 Testing

The package includes comprehensive tests covering:

- **Environment Loading**: Correct loading based on `ENVIRONMENT` variable
- **Error Handling**: Missing environments, files, and import errors
- **Lazy Loading**: Modules are loaded only when accessed
- **Caching**: Modules are cached after first load
- **Dynamic Behavior**: Different environments load different configurations

Run tests:
```bash
# Run all environment tests
python -m pytest environment/tests/ -v

# Run with coverage
python -m pytest environment/tests/ --cov=environment --cov-report=term-missing -v

# Run specific test file
python -m pytest environment/tests/test_loader.py -v
```

## 🔧 Advanced Usage

### Conditional Configuration

You can create conditional logic within your configuration files:

```python
# environment/envs/my-env/settings.py
import os

# Base settings
api_timeout = 30
enable_debug_mode = True

# Conditional settings based on sub-environment
if os.environ.get("SUB_ENV") == "integration":
    api_timeout = 60
    enable_debug_mode = False
```

### Dynamic Host Building

```python
# environment/envs/my-env/hosts.py
import os

# Base domain
base_domain = os.environ.get("BASE_DOMAIN", "example.com")

# Build hosts dynamically
game_web = f"https://game.{base_domain}"
game_api = f"https://api.{base_domain}"
backoffice_url = f"https://backoffice.{base_domain}"
```

### Environment-Specific Imports

```python
# environment/envs/production/settings.py
from some_production_only_module import ProductionConfig

# Use production-specific configurations
database_pool_size = ProductionConfig.DB_POOL_SIZE
cache_backend = ProductionConfig.REDIS_CLUSTER
```

## 🐛 Error Handling

The package provides comprehensive error handling with detailed logging for different scenarios:

### Missing Environment
When an environment folder doesn't exist, the package logs an error and raises an ImportError:

```python
# ENVIRONMENT=nonexistent-env
from environment import hosts  
# ERROR: Environment 'nonexistent-env' does not exist. Available environments: ['phoenix-staging', 'ks-staging']
# ImportError: Environment 'nonexistent-env' does not exist. Available environments: ['phoenix-staging', 'ks-staging']
```

### Missing Configuration Files
When a required configuration file (hosts.py or settings.py) is missing:

```python
# Missing hosts.py in environment folder
from environment import hosts  
# ERROR: Module 'hosts.py' not found in environment 'my-env'
# ImportError: Module 'hosts.py' not found in environment 'my-env'
```

### Missing Properties
When accessing a property that doesn't exist in the configuration, the package logs a warning and returns None:

```python
from environment import hosts, settings

# Access non-existent properties
missing_host = hosts.nonexistent_host
# WARNING: Property 'nonexistent_host' not found in hosts for environment 'phoenix-staging'. Returning None.
print(missing_host)  # None

missing_setting = settings.nonexistent_setting  
# WARNING: Property 'nonexistent_setting' not found in settings for environment 'phoenix-staging'. Returning None.
print(missing_setting)  # None
```

### Import Errors
For syntax errors or other issues in configuration files:

```python
# Syntax error in configuration file
from environment import settings  
# ERROR: Failed to import environment.envs.my-env.settings: <detailed error>
# ImportError: Failed to import environment.envs.my-env.settings: <detailed error>
```

## 📋 Best Practices

1. **Consistent Structure**: Keep the same variable names across all environments
2. **Documentation**: Document what each configuration variable does
3. **Validation**: Add validation for critical configuration values
4. **Defaults**: Provide sensible defaults for optional settings
5. **Security**: Never commit sensitive data like passwords or API keys
6. **Testing**: Test your configurations with the provided test framework

## 🔗 Integration

The environment package integrates seamlessly with the project's logger:

```python
from environment import hosts, settings
from logger import log

log.info(f"Connecting to game service at {hosts.game_web}")
log.debug(f"Using API timeout of {settings.api_timeout} seconds")
```

## 📝 Sample Scripts

The `samples/` directory contains example scripts:

- **`print_host.py`**: Basic usage example showing how to access hosts and settings
- **`demo_environment.py`**: Comprehensive demonstration of environment switching
- **`demo_error_handling.py`**: Examples of error handling and logging behavior

Run samples:
```bash
cd environment/samples
PYTHONPATH=../.. python3 print_host.py
PYTHONPATH=../.. python3 demo_environment.py  
PYTHONPATH=../.. python3 demo_error_handling.py
```

## 🤝 Contributing

When adding new environments or modifying existing ones:

1. Follow the existing naming conventions
2. Add appropriate documentation
3. Test your changes with the test suite
4. Update this README if adding new features

## 🔍 Troubleshooting

### Common Issues

**Import Errors**: Make sure your environment folder exists and contains both `hosts.py` and `settings.py`

**Module Not Found**: Check that the `ENVIRONMENT` variable matches your folder name exactly

**Configuration Not Loading**: Verify that your configuration files have valid Python syntax

**Logging Issues**: Ensure the logger package is properly configured

### Debug Mode

Enable debug logging to see detailed information about environment loading:

```bash
export LOGGER_LOG_LEVEL=DEBUG
python your_app.py
```

This will show which environment is being loaded and any issues during the loading process.
