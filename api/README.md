# API Testing Framework 🌐

Comprehensive API testing framework with client libraries, endpoint definitions, automated validation, and multi-tenant support.

## Overview

The API framework provides structured testing for REST APIs with automatic serialization, authentication handling, response validation, and integration with the test data factory.

## Architecture

```
api/
├── clients/                 # API client implementations
│   ├── base.py             # Base API client
│   ├── player_client.py    # Player-specific API client
│   ├── operator_client.py  # Operator API client
│   └── features/           # Feature-specific clients
├── endpoints/              # Endpoint definitions
│   ├── access/            # Access control endpoints
│   ├── player_notes/      # Player notes endpoints
│   ├── wallet/            # Wallet operations
│   └── ...
├── executor/              # Test execution engine
└── postman/              # Postman collection exports
```

## Features

- **Multi-Tenant Support**: Kansas, Catalyst, and other tenants
- **Authentication**: Automatic token management and refresh
- **Validation**: Response schema validation and assertions
- **Data Integration**: Integration with data factory for test data
- **Error Handling**: Comprehensive error handling and retries
- **Documentation**: Auto-generated API documentation

## Usage Examples

### Basic API Test
```python
def test_player_creation(player_client):
    """Test player creation via API."""
    player_data = PlayerFactory.build()
    
    response = player_client.create_player(player_data)
    
    assert response.status_code == 201
    assert response.json()['email'] == player_data.email
    assert response.json()['status'] == 'active'
```

### Authentication Testing
```python
def test_player_authentication(player_client):
    """Test player authentication flow."""
    # Register player
    player = PlayerFactory.build()
    registration_response = player_client.register(player)
    assert registration_response.status_code == 201
    
    # Login
    login_response = player_client.login(
        email=player.email,
        password=player.password
    )
    assert login_response.status_code == 200
    assert 'access_token' in login_response.json()
    
    # Access protected resource
    profile_response = player_client.get_profile()
    assert profile_response.status_code == 200
```

### Wallet Operations
```python
def test_wallet_operations(player_client):
    """Test wallet deposit and withdrawal."""
    # Setup authenticated player
    player_client.authenticate()
    
    # Get initial balance
    balance_response = player_client.wallet.get_balance()
    initial_balance = balance_response.json()['balance']
    
    # Deposit funds
    deposit_response = player_client.wallet.deposit(100.00)
    assert deposit_response.status_code == 200
    
    # Verify balance update
    new_balance_response = player_client.wallet.get_balance()
    new_balance = new_balance_response.json()['balance']
    assert new_balance == initial_balance + 100.00
```

## Client Architecture

### Base Client
```python
class BaseApiClient:
    def __init__(self, base_url: str, tenant: str):
        self.base_url = base_url
        self.tenant = tenant
        self.session = requests.Session()
        self.auth_token = None
    
    def authenticate(self, credentials):
        """Handle authentication and token management."""
        pass
    
    def request(self, method, endpoint, **kwargs):
        """Make authenticated API request."""
        pass
```

### Player Client
```python
class PlayerApiClient(BaseApiClient):
    def __init__(self, player: Player):
        super().__init__(
            base_url=settings.api_base_url,
            tenant=settings.tenant
        )
        self.player = player
        self.wallet = WalletClient(self)
        self.games = GamesClient(self)
        self.account = AccountClient(self)
    
    def register(self):
        """Register new player account."""
        return self.post('/players/register', json=self.player.to_dict())
    
    def login(self):
        """Authenticate player."""
        response = self.post('/auth/login', json={
            'email': self.player.email,
            'password': self.player.password
        })
        
        if response.status_code == 200:
            self.auth_token = response.json()['access_token']
            self.session.headers.update({
                'Authorization': f'Bearer {self.auth_token}'
            })
        
        return response
```

## Endpoint Definitions

### Structured Endpoint Organization
```python
# api/endpoints/wallet/deposits.py
class DepositsEndpoint:
    base_path = "/wallet/deposits"
    
    @staticmethod
    def create_deposit(amount: float, payment_method_id: str):
        return {
            'method': 'POST',
            'path': '/wallet/deposits',
            'json': {
                'amount': amount,
                'payment_method_id': payment_method_id
            }
        }
    
    @staticmethod
    def get_deposit_history():
        return {
            'method': 'GET',
            'path': '/wallet/deposits/history'
        }
```

## Response Validation

### Schema Validation
```python
from pydantic import BaseModel

class PlayerResponse(BaseModel):
    id: str
    email: str
    status: str
    created_at: str
    balance: float

def test_player_creation_schema(player_client):
    """Test player creation response schema."""
    player_data = PlayerFactory.build()
    response = player_client.create_player(player_data)
    
    # Validate response schema
    player_response = PlayerResponse(**response.json())
    assert player_response.email == player_data.email
```

### Custom Assertions
```python
class ApiAssertions:
    @staticmethod
    def assert_success_response(response, expected_status=200):
        assert response.status_code == expected_status
        assert 'error' not in response.json()
    
    @staticmethod
    def assert_error_response(response, expected_status=400):
        assert response.status_code == expected_status
        assert 'error' in response.json()
        assert 'message' in response.json()

def test_invalid_player_data(player_client):
    """Test API error handling."""
    invalid_data = {'email': 'invalid-email'}
    response = player_client.create_player(invalid_data)
    
    ApiAssertions.assert_error_response(response, 400)
    assert 'email' in response.json()['errors']
```

## Multi-Tenant Configuration

### Tenant-Specific Clients
```python
class TenantApiClientFactory:
    @staticmethod
    def create_player_client(tenant: str) -> PlayerApiClient:
        if tenant.lower() == 'kansas':
            return KansasPlayerApiClient()
        elif tenant.lower() == 'catalyst':
            return CatalystPlayerApiClient()
        else:
            return DefaultPlayerApiClient()

# Usage
player_client = TenantApiClientFactory.create_player_client(settings.tenant)
```

## Integration Testing

### API + Database Validation
```python
def test_player_creation_with_database(player_client, database):
    """Test player creation with database validation."""
    player_data = PlayerFactory.build()
    
    # Create via API
    api_response = player_client.create_player(player_data)
    assert api_response.status_code == 201
    
    # Validate in database
    db_player = database.players.find_by_email(player_data.email)
    assert db_player is not None
    assert db_player.status == 'active'
    assert db_player.email == player_data.email
```

### API + UI Validation
```python
def test_player_api_ui_consistency(player_client, visitor):
    """Test consistency between API and UI."""
    # Create player via API
    player_data = PlayerFactory.build()
    api_response = player_client.create_player(player_data)
    assert api_response.status_code == 201
    
    # Verify in UI
    visitor.ui.open()
    visitor.ui.authentication.login(
        email=player_data.email,
        password=player_data.password
    )
    
    ui_profile = visitor.ui.account.get_profile()
    api_profile = player_client.get_profile().json()
    
    assert ui_profile.email == api_profile['email']
    assert ui_profile.balance == api_profile['balance']
```

## Configuration

### Environment Configuration
```python
# Environment-specific API settings
API_SETTINGS = {
    'pgp_sit': {
        'base_url': 'https://api-sit.example.com',
        'timeout': 30,
        'retries': 3
    },
    'pgp_prod': {
        'base_url': 'https://api.example.com',
        'timeout': 60,
        'retries': 1
    }
}
```

### Pytest Fixtures
```python
@pytest.fixture
def player_client():
    """Create authenticated player API client."""
    player = PlayerFactory.build()
    client = PlayerApiClient(player)
    
    # Register and authenticate
    client.register()
    client.login()
    
    yield client
    
    # Cleanup
    client.cleanup()

@pytest.fixture
def operator_client():
    """Create authenticated operator API client."""
    operator = OperatorFactory.build()
    client = OperatorApiClient(operator)
    client.authenticate()
    
    yield client
    client.cleanup()
```

## Best Practices

1. **Use Factories**: Generate test data with data factories
2. **Validate Responses**: Always validate response schemas
3. **Handle Authentication**: Implement proper token management
4. **Test Error Cases**: Include negative test scenarios
5. **Clean Up**: Properly clean up test data
6. **Environment Awareness**: Support multiple environments
7. **Retry Logic**: Implement retry for flaky endpoints

## Performance Testing

```python
import time
import statistics

def test_api_performance(player_client):
    """Test API response times."""
    response_times = []
    
    for _ in range(10):
        start_time = time.time()
        response = player_client.get_profile()
        end_time = time.time()
        
        assert response.status_code == 200
        response_times.append(end_time - start_time)
    
    avg_response_time = statistics.mean(response_times)
    assert avg_response_time < 2.0  # Less than 2 seconds average
```

## Error Handling

```python
class ApiException(Exception):
    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code
        self.message = response.json().get('message', 'Unknown error')
        super().__init__(self.message)

class BaseApiClient:
    def request(self, method, endpoint, **kwargs):
        response = self.session.request(method, endpoint, **kwargs)
        
        if not response.ok:
            raise ApiException(response)
        
        return response
```
