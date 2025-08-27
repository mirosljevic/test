# API Clients Package

A comprehensive, modular API client system for different service endpoints with feature-based organization and placeholder implementations ready for integration with the API executor framework.

## 🏗️ Overview

The API clients package provides three specialized client types, each tailored for specific use cases:

- **WebClient**: Player-facing endpoints for web applications
- **CCClient**: Operator-facing endpoints for customer care and back-office operations  
- **S2SClient**: Service-to-service endpoints for internal microservice communication

Each client is composed of modular feature APIs that handle related functionality, providing clean separation of concerns and easy extensibility.

## 📁 Package Structure

```
api/clients/
├── __init__.py              # Package exports
├── base.py                  # Shared BaseAPIClient functionality
├── web_client.py            # Player-facing API client
├── cc_client.py             # Operator-facing API client
├── s2s_client.py            # Service-to-service API client
├── features/                # Modular feature implementations
│   ├── __init__.py          # Feature exports
│   ├── authentication.py   # Login/logout operations
│   ├── registration.py     # User registration and onboarding
│   ├── bonus.py            # Promotions and rewards
│   ├── documents.py        # Document upload and verification
│   ├── dgs.py              # Draw game services
│   └── instants.py         # Instant game operations
├── samples/                 # Usage examples
│   ├── login_player.py      # Player authentication demo
│   └── register_player.py   # Player registration demo
└── tests/                   # Comprehensive test suite
    ├── test_web_client.py   # WebClient tests
    └── test_authentication_feature.py # Feature tests
```

## 🚀 Quick Start

### Basic Usage

```python
from api.clients import WebClient, CCClient, S2SClient

# Player-facing operations
web_client = WebClient()
web_client.authentication.login(username="player@example.com", password="password")
web_client.registration.register(user_data={"email": "new@example.com"})

# Operator operations  
cc_client = CCClient(token="operator_token")
cc_client.documents.approve_document("doc_123", operator_id="op_456")

# Service-to-service operations
s2s_client = S2SClient(token="service_token") 
s2s_client.bonus.claim_bonus("bonus_789", player_id="player_123")
```

### Integration with Actors

The clients are designed to be pluggable into Actor objects:

```python
from actors import Player
from api.clients import WebClient

# Create player actor with API client
player = Player()
player.api = WebClient()

# Use through actor
player.api.authentication.login(username=player.email, password=player.password)
```

## 🎯 Client Types

### WebClient - Player-Facing Operations

The `WebClient` handles all operations that players perform through web interfaces:

**Available Features:**
- `authentication`: Login, logout, password management
- `registration`: Account creation, email verification, profile setup
- `bonus`: View and claim bonuses, promotion management
- `documents`: Upload and track document verification
- `dgs`: Purchase draw game tickets, check results
- `instants`: Play instant games, claim prizes

**Example Usage:**
```python
from api.clients import WebClient

client = WebClient(base_url="https://api.gaming-site.com")

# Player login
response = client.authentication.login(
    username="player@example.com",
    password="secure_password"
)

# Set token for authenticated requests
if response.get("token"):
    client.set_token(response["token"])

# Purchase lottery ticket
ticket = client.dgs.purchase_ticket(
    game_id="powerball",
    numbers=[1, 15, 23, 42, 55],
    player_id="player_123"
)
```

### CCClient - Operator Operations

The `CCClient` provides operator-facing functionality for customer care and back-office operations:

**Available Features:**
- `authentication`: Operator login and session management
- `bonus`: Bonus administration and management
- `documents`: Document verification and approval
- `dgs`: Draw game administration
- `instants`: Instant game management

**Example Usage:**
```python
from api.clients import CCClient

client = CCClient(
    base_url="https://backoffice.gaming-site.com",
    token="operator_session_token"
)

# Approve player document
approval = client.documents.approve_document(
    document_id="doc_456",
    operator_id="op_789"
)

# Check draw game results
results = client.dgs.get_draw_results(
    game_id="daily_lotto",
    draw_date="2024-07-14"
)
```

### S2SClient - Service Communication

The `S2SClient` handles internal service-to-service communication with extended timeouts and service identification:

**Available Features:**
- All features available (full access for internal operations)
- Extended timeout settings for service communication
- Service identification headers
- Health check capabilities

**Example Usage:**
```python
from api.clients import S2SClient

client = S2SClient(
    base_url="https://internal-api.gaming-services.com",
    token="service_auth_token",
    timeout=60
)

# Internal health check
health = client.health_check()

# Process bonus from another service
bonus_result = client.bonus.claim_bonus(
    bonus_id="auto_bonus_123",
    player_id="player_from_service_a"
)
```

## 🔧 Feature Modules

Each feature module represents a logical grouping of related API endpoints:

### AuthenticationAPI
- `login()`: User authentication
- `logout()`: Session termination
- `validate_token()`: Token verification
- `refresh_token()`: Token renewal
- `change_password()`: Password updates
- `forgot_password()`: Password reset initiation
- `reset_password()`: Password reset completion

### RegistrationAPI  
- `register()`: New user registration
- `verify_email()`: Email address verification
- `resend_verification()`: Resend verification email
- `activate_account()`: Account activation
- `check_username_availability()`: Username validation
- `check_email_availability()`: Email validation
- `complete_profile()`: Profile completion

### BonusAPI
- `get_available_bonuses()`: Available promotions
- `claim_bonus()`: Bonus redemption
- `get_bonus_history()`: Bonus transaction history
- `cancel_bonus()`: Bonus cancellation
- `get_promotion_details()`: Promotion information
- `opt_in_promotion()`: Promotion enrollment
- `get_loyalty_points()`: Loyalty program status

### DocumentsAPI
- `upload_document()`: Document submission
- `get_document_status()`: Verification status
- `list_documents()`: Document inventory
- `delete_document()`: Document removal
- `approve_document()`: Operator approval
- `reject_document()`: Operator rejection
- `get_document_requirements()`: Required documents

### DGSAPI (Draw Game Services)
- `purchase_ticket()`: Lottery ticket purchase
- `get_draw_results()`: Draw outcome retrieval
- `get_ticket_status()`: Ticket status check
- `get_player_tickets()`: Player ticket history
- `claim_prize()`: Prize redemption
- `get_game_info()`: Game information
- `get_available_games()`: Available games list
- `get_draw_schedule()`: Draw scheduling

### InstantsAPI
- `launch_game()`: Game session initiation
- `play_game()`: Game action execution
- `get_game_result()`: Session outcome
- `claim_instant_prize()`: Prize collection
- `get_available_instant_games()`: Available games
- `get_game_history()`: Play history
- `get_instant_game_info()`: Game details
- `end_session()`: Session termination

## 🔧 Configuration and Customization

### Base URLs

Each client type has default base URLs that can be overridden:

```python
# Use default URLs
web_client = WebClient()  # https://web-api.example.com
cc_client = CCClient()    # https://cc-api.example.com  
s2s_client = S2SClient()  # https://s2s-api.example.com

# Override with custom URLs
web_client = WebClient(base_url="https://prod-api.yourdomain.com")
```

### Authentication

All clients support token-based authentication:

```python
# Set token during initialization
client = WebClient(token="your_auth_token")

# Set token after initialization
client = WebClient()
client.set_token("your_auth_token")

# Clear token
client.clear_token()
```

### Timeouts

Configure request timeouts based on client type:

```python
web_client = WebClient(timeout=30)    # Default for user operations
cc_client = CCClient(timeout=45)      # Longer for operator operations
s2s_client = S2SClient(timeout=60)    # Longest for service operations
```

## 📊 Logging Integration

The package integrates with the logger package for comprehensive debugging:

```python
import logging
from api.clients import WebClient

# Enable debug logging
logging.getLogger().setLevel(logging.DEBUG)

# All operations are logged
client = WebClient()
# DEBUG: Initialized WebClient with base_url: https://web-api.example.com

client.authentication.login(username="test", password="pass")  
# DEBUG: Calling login() on AuthenticationAPI for user: test
```

## 📂 Sample Scripts

### Login Player Sample

```python
# api/clients/samples/login_player.py
from api.clients import WebClient

client = WebClient()
response = client.authentication.login(
    username="john.doe@example.com",
    password="player_password_123"
)

if response.get("token"):
    client.set_token(response["token"])
    print("✅ Login successful")
```

### Register Player Sample

```python
# api/clients/samples/register_player.py  
from api.clients import WebClient

client = WebClient()

# Check availability
email_available = client.registration.check_email_availability(
    email="new.player@example.com"
)

# Register user
if email_available:
    response = client.registration.register(user_data={
        "username": "new_player_123",
        "email": "new.player@example.com", 
        "password": "secure_password"
    })
```

## 🧪 Testing

The package includes comprehensive pytest-based tests:

```bash
# Run all tests
python -m pytest api/clients/tests/ -v

# Run specific test files
python -m pytest api/clients/tests/test_web_client.py -v
python -m pytest api/clients/tests/test_authentication_feature.py -v

# Run with coverage
python -m pytest api/clients/tests/ --cov=api.clients --cov-report=term-missing
```

### Test Coverage

- **Client Tests**: Initialization, feature integration, token management
- **Feature Tests**: Method calls, parameter handling, response format
- **Mock Integration**: External dependency mocking for isolated testing
- **Logger Integration**: Verification of debug logging calls

## 🔌 Integration Points

### API Executor Integration

All feature modules are designed to integrate with the API executor:

```python
# Current placeholder implementation
def login(self, username=None, password=None, **kwargs):
    log.debug(f"Calling login() on AuthenticationAPI for user: {username}")
    # TODO: Implement actual API call using self.executor
    return {"status": "placeholder", "method": "login"}

# Future implementation with API executor
def login(self, username=None, password=None, **kwargs):
    log.debug(f"Calling login() on AuthenticationAPI for user: {username}")
    
    @api
    def login_request():
        return {
            "host": self.base_url,
            "method": "POST", 
            "endpoint": "/auth/login",
            "json": {
                "username": username,
                "password": password,
                **kwargs
            }
        }
    
    return login_request()
```

### Actor Pattern Integration

Designed for seamless integration with Actor objects:

```python
from actors import Player
from api.clients import WebClient

class Player:
    def __init__(self):
        self.api = WebClient()
        
    def login(self):
        return self.api.authentication.login(
            username=self.email,
            password=self.password  
        )
```

### Environment Integration

Supports environment-based configuration:

```python
from environment import hosts
from api.clients import WebClient

# Use environment-specific URLs
client = WebClient(base_url=hosts.game_api)
```

## 🛠️ Development Guidelines

### Adding New Features

1. Create feature module in `features/` directory
2. Follow existing pattern with placeholder methods
3. Add comprehensive logging
4. Update client classes to include new feature
5. Add tests for new functionality

### Adding New Clients

1. Inherit from `BaseAPIClient`
2. Override `_get_default_base_url()`
3. Initialize appropriate feature modules
4. Implement `get_client_features()`
5. Add client to package exports

### Method Implementation Pattern

```python
def method_name(self, param1, param2=None):
    """
    Method description.
    
    Args:
        param1 (type): Description
        param2 (type, optional): Description
        
    Returns:
        dict: Response description (placeholder)
    """
    log.debug(f"Calling method_name() on FeatureAPI")
    # TODO: Implement actual API call using self.executor
    return {"status": "placeholder", "method": "method_name"}
```

## 🔄 Future Enhancements

- **Real API Implementation**: Replace placeholders with actual API executor calls
- **Response Validation**: Add response schema validation
- **Retry Logic**: Implement automatic retry for failed requests
- **Caching**: Add response caching for appropriate endpoints
- **Rate Limiting**: Implement client-side rate limiting
- **Metrics**: Add performance and usage metrics
- **Configuration Management**: Environment-based client configuration

## 🤝 Integration with Framework

This package is designed to integrate seamlessly with the broader automation framework:

- **Logger Package**: Uses framework logging for consistent output
- **Environment Package**: Supports environment-based configuration  
- **Models Package**: Ready for integration with typed model responses
- **API Executor**: Placeholder implementations ready for executor integration
- **Actor Pattern**: Designed for actor composition patterns

The modular, feature-based design ensures clean separation of concerns while maintaining flexibility for different client types and use cases.

---

For more information about the broader automation framework, see the main project [README](../../README.md).
