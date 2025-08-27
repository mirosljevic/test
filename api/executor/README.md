# API Executor Package

A powerful and flexible HTTP request execution framework with comprehensive logging and decorator-based automation. This package provides both direct API execution and decorator-based request automation for seamless API integration.

## Features

- **Direct API Execution**: Execute HTTP requests with full control using the `ApiExecutor` class
- **Decorator-based Automation**: Use the `@api` decorator for automatic request execution
- **Comprehensive Logging**: Built-in logging for all requests and responses
- **Flexible Configuration**: Support for various HTTP methods, headers, and authentication
- **Error Handling**: Robust error handling with detailed logging
- **Mock Support**: Easy testing with mock support

## Installation

The package is part of the test automation framework and requires the following dependencies:

```bash
pip install requests
```

## Quick Start

### Basic Usage with ApiExecutor

```python
from api.executor import ApiExecutor

# Create and execute a GET request
executor = ApiExecutor(
    host="https://api.example.com",
    method="GET",
    endpoint="/users/1"
)

response = executor.execute()
print(f"Status: {response.status_code}")
print(f"Data: {response.json()}")
```

### Using the @api Decorator

```python
from api.executor import api

@api
def get_user(user_id):
    return {
        "host": "https://api.example.com",
        "method": "GET",
        "endpoint": f"/users/{user_id}"
    }

# Execute the request
response = get_user(123)
print(f"User: {response.json()}")
```

### POST Request with Data

```python
from api.executor import ApiExecutor

executor = ApiExecutor(
    host="https://api.example.com",
    method="POST",
    endpoint="/users",
    data={"name": "John Doe", "email": "john@example.com"}
)

response = executor.execute()
print(f"Created user: {response.json()}")
```

## API Reference

### ApiExecutor Class

The main class for executing HTTP requests with full control over request parameters.

#### Constructor Parameters

- `host` (str): The base URL for the API
- `method` (str): HTTP method (GET, POST, PUT, DELETE, etc.)
- `endpoint` (str): The API endpoint path
- `data` (dict, optional): Request body data
- `headers` (dict, optional): Additional HTTP headers
- `timeout` (int, optional): Request timeout in seconds (default: 30)
- `bearer_token` (str, optional): Bearer token for authentication
- `basic_auth` (tuple, optional): Basic authentication (username, password)

#### Methods

- `execute()`: Execute the HTTP request and return the response

#### Example Usage

```python
from api.executor import ApiExecutor

# GET request
executor = ApiExecutor(
    host="https://api.example.com",
    method="GET",
    endpoint="/users",
    headers={"Accept": "application/json"}
)

response = executor.execute()

# POST request with authentication
executor = ApiExecutor(
    host="https://api.example.com",
    method="POST",
    endpoint="/users",
    data={"name": "Jane Doe"},
    bearer_token="your_token_here"
)

response = executor.execute()
```

### @api Decorator

A decorator that automatically creates and executes ApiExecutor instances based on the parameters returned by your function.

#### Function Return Format

Your decorated function should return a dictionary with ApiExecutor parameters:

```python
@api
def api_function():
    return {
        "host": "https://api.example.com",
        "method": "GET",
        "endpoint": "/endpoint",
        "data": {"key": "value"},          # optional
        "headers": {"Custom": "Header"},   # optional
        "bearer_token": "token",           # optional
        "timeout": 60                      # optional
    }
```

#### Example Usage

```python
from api.executor import api

@api
def get_user_profile(user_id):
    return {
        "host": "https://api.example.com",
        "method": "GET",
        "endpoint": f"/users/{user_id}/profile",
        "bearer_token": "your_token_here"
    }

@api
def create_user(name, email):
    return {
        "host": "https://api.example.com",
        "method": "POST",
        "endpoint": "/users",
        "data": {"name": name, "email": email},
        "headers": {"Content-Type": "application/json"}
    }

# Usage
user_response = get_user_profile(123)
create_response = create_user("John Doe", "john@example.com")
```

## Authentication

The package supports multiple authentication methods:

### Bearer Token Authentication

```python
executor = ApiExecutor(
    host="https://api.example.com",
    method="GET",
    endpoint="/protected",
    bearer_token="your_jwt_token_here"
)
```

### Basic Authentication

```python
executor = ApiExecutor(
    host="https://api.example.com",
    method="GET",
    endpoint="/protected",
    basic_auth=("username", "password")
)
```

### Custom Headers

```python
executor = ApiExecutor(
    host="https://api.example.com",
    method="GET",
    endpoint="/protected",
    headers={"Authorization": "Custom auth_token"}
)
```

## Error Handling

The package includes comprehensive error handling with detailed logging:

```python
from api.executor import ApiExecutor

try:
    executor = ApiExecutor(
        host="https://api.example.com",
        method="GET",
        endpoint="/users"
    )
    response = executor.execute()
    
    if response.status_code == 200:
        print("Success!")
    else:
        print(f"Error: {response.status_code}")
        
except Exception as e:
    print(f"Request failed: {e}")
```

## Logging

The package integrates with the logger package for comprehensive request/response logging:

```python
from logger import log
from api.executor import ApiExecutor

log.set_level("DEBUG")

executor = ApiExecutor(
    host="https://api.example.com",
    method="GET",
    endpoint="/users"
)

response = executor.execute()  # Will log request details and response
```

## Testing

The package includes comprehensive tests and supports mocking for unit tests:

```python
from unittest.mock import Mock, patch
from api.executor import ApiExecutor

@patch("api.executor.executor.requests.request")
def test_api_request(mock_request):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Test"}
    mock_request.return_value = mock_response

    executor = ApiExecutor(
        host="https://api.example.com",
        method="GET",
        endpoint="/test"
    )
    
    response = executor.execute()
    
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Test"}
```

Run the test suite:

```bash
# Run all API executor tests
pytest api/executor/tests/ -v

# Run specific test
pytest api/executor/tests/test_api_executor.py::TestApiExecutor::test_basic_get_request -v
```

## Examples

See the `samples/` directory for practical examples:

- `basic_usage.py` - Basic ApiExecutor usage
- `decorator_usage.py` - @api decorator examples

## Common Use Cases

### RESTful API Integration

```python
from api.executor import api

@api
def get_users():
    return {
        "host": "https://api.example.com",
        "method": "GET",
        "endpoint": "/users"
    }

@api
def get_user(user_id):
    return {
        "host": "https://api.example.com",
        "method": "GET",
        "endpoint": f"/users/{user_id}"
    }

@api
def create_user(user_data):
    return {
        "host": "https://api.example.com",
        "method": "POST",
        "endpoint": "/users",
        "data": user_data
    }

@api
def update_user(user_id, user_data):
    return {
        "host": "https://api.example.com",
        "method": "PUT",
        "endpoint": f"/users/{user_id}",
        "data": user_data
    }

@api
def delete_user(user_id):
    return {
        "host": "https://api.example.com",
        "method": "DELETE",
        "endpoint": f"/users/{user_id}"
    }
```

### API with Authentication

```python
from api.executor import api

AUTH_TOKEN = "your_auth_token_here"

@api
def get_protected_data():
    return {
        "host": "https://api.example.com",
        "method": "GET",
        "endpoint": "/protected",
        "bearer_token": AUTH_TOKEN
    }

@api
def post_protected_data(data):
    return {
        "host": "https://api.example.com",
        "method": "POST",
        "endpoint": "/protected",
        "data": data,
        "bearer_token": AUTH_TOKEN
    }
```

## Performance Considerations

- **Connection Pooling**: The underlying requests library handles connection pooling automatically
- **Timeout Configuration**: Always set appropriate timeout values for your use case
- **Error Retry**: Consider implementing retry logic for transient failures
- **Logging Level**: Set appropriate logging levels in production to avoid performance impact

## Package Structure

```
api/executor/
├── __init__.py              # Package exports
├── executor.py             # ApiExecutor class implementation
├── decorator.py            # @api decorator implementation
├── status.py               # Status code utilities
├── samples/
│   ├── basic_usage.py      # Basic usage examples
│   └── decorator_usage.py  # Decorator usage examples
└── tests/
    └── test_api_executor.py # Comprehensive test suite
```

## Dependencies

- `requests` - For HTTP request handling
- `logger` - For request/response logging
- `unittest.mock` - For testing support

## Contributing

When adding new features:

1. Follow the existing code structure and patterns
2. Add comprehensive tests for new functionality
3. Update the README with new examples
4. Ensure all tests pass
5. Add proper error handling and logging

## License

This package is part of the test automation framework and follows the same license terms.
