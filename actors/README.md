# Test Actors Framework 🎭

The actors framework provides test personas representing different user types with role-specific capabilities, data generation, and behavior patterns.

## Overview

Actors are high-level test entities that encapsulate user behavior, credentials, and context. They provide a clean interface for test scenarios while handling complex setup and teardown operations.

## Available Actors

### PlayerActor 👤
Represents a game player with capabilities for:
- Account registration and authentication
- Game interaction (instant games, draws)
- Wallet operations (deposits, withdrawals)
- Account management
- Profile updates

### OperatorActor 🔧
Represents an operator user with capabilities for:
- Admin panel access
- Player management
- Game configuration
- Reports and analytics
- System administration

## Architecture

```python
# Base Actor
class BaseActor:
    def __init__(self):
        self.context = {}
        self.credentials = {}
    
    def setup(self):
        """Setup actor state"""
        pass
    
    def cleanup(self):
        """Cleanup actor resources"""
        pass

# Player Actor Implementation
class PlayerActor(BaseActor):
    def __init__(self):
        super().__init__()
        self.player = PlayerFactory.generate()
        self.ui = PlayerFacade(page, self.player)
        self.api = PlayerApiClient(self.player)
```

## Usage Examples

### Basic Player Test
```python
def test_player_workflow(visitor: PlayerActor):
    """Test complete player workflow."""
    # Registration
    visitor.ui.open()
    registration_result = visitor.ui.registration.register()
    assert registration_result.success
    
    # Login
    login_result = visitor.ui.authentication.login()
    assert login_result.success
    
    # Account verification
    account_info = visitor.ui.account.get_details()
    assert account_info.email == visitor.player.email
```

### Cross-Platform Testing
```python
@pytest.mark.parametrize("device", ["desktop", "ipad_air", "mobile"])
def test_player_registration_cross_platform(visitor, device):
    """Test player registration across different devices."""
    os.environ['DEVICE'] = device
    
    visitor.ui.open()
    result = visitor.ui.registration.register()
    
    assert result.success
    assert visitor.ui.account.is_logged_in()
```

### API + UI Validation
```python
def test_player_data_consistency(visitor: PlayerActor):
    """Test data consistency between API and UI."""
    # Create via API
    api_response = visitor.api.registration.create_account()
    assert api_response.status_code == 201
    
    # Verify in UI
    visitor.ui.open()
    visitor.ui.authentication.login()
    account_details = visitor.ui.account.get_details()
    
    assert account_details.email == visitor.player.email
    assert account_details.status == "active"
```

## Configuration

### Pytest Fixtures
```python
@pytest.fixture
def visitor(page: Page) -> PlayerActor:
    """Create a player actor for testing."""
    actor = PlayerActor(page)
    yield actor
    actor.cleanup()

@pytest.fixture
def operator(page: Page) -> OperatorActor:
    """Create an operator actor for testing."""
    actor = OperatorActor(page)
    yield actor
    actor.cleanup()
```

### Environment-Specific Actors
```python
# Different actors for different environments
if settings.environment == "pgp_sit":
    actor = KansasPlayerActor(page)
elif settings.environment == "catalyst_sit":
    actor = CatalystPlayerActor(page)
```

## Data Generation

Actors integrate with the data factory for realistic test data:

```python
class PlayerActor:
    def __init__(self, page: Page):
        self.player = PlayerFactory.build(
            tenant=settings.tenant,
            state="KS" if settings.tenant == "kansas" else "CA"
        )
        self.credit_card = CreditCardFactory.build()
        self.bank_account = BankAccountFactory.build()
```

## Device Awareness

Actors automatically adapt to different devices and layouts:

```python
class PlayerActor:
    def register(self):
        """Register player with device-aware UI."""
        layout = self.ui.home_page.layout
        
        if layout == "mobile":
            return self._mobile_registration()
        elif layout == "tablet":
            return self._tablet_registration()
        else:
            return self._desktop_registration()
```

## Files Structure

```
actors/
├── __init__.py              # Actor exports
├── base.py                  # Base actor functionality
├── player.py               # Player actor implementation
├── operator.py             # Operator actor implementation
└── README.md               # This file
```

## Best Practices

1. **Single Responsibility**: Each actor should represent one user type
2. **Stateful**: Actors maintain context throughout test execution
3. **Cleanup**: Always implement proper cleanup in fixtures
4. **Data Isolation**: Each actor gets fresh test data
5. **Device Agnostic**: Actors work across all supported devices

## Extending Actors

### Creating Custom Actors
```python
class AdminActor(BaseActor):
    def __init__(self, page: Page):
        super().__init__(page)
        self.admin = AdminFactory.build()
        self.ui = AdminFacade(page, self.admin)
        self.api = AdminApiClient(self.admin)
    
    def access_admin_panel(self):
        """Access admin panel with proper credentials."""
        return self.ui.login.admin_login()
```

### Actor Mixins
```python
class WalletMixin:
    def deposit_funds(self, amount: float):
        """Add funds to player wallet."""
        return self.ui.wallet.deposit(amount)
    
    def withdraw_funds(self, amount: float):
        """Withdraw funds from wallet."""
        return self.ui.wallet.withdraw(amount)

class PlayerActor(BaseActor, WalletMixin):
    # Inherits wallet functionality
    pass
```

## Integration

Actors integrate seamlessly with:
- **UI Framework**: Page objects and facades
- **API Framework**: Client libraries
- **Data Factory**: Test data generation
- **Database**: Direct database access
- **Email Service**: Email verification
- **Dashboard**: Real-time monitoring
