# Data Factory Package

A comprehensive factory package for generating realistic test data using the Faker library. This package provides factory functions for creating test instances of various data models with tenant-specific customizations.

## Features

- **Realistic Data Generation**: Uses Faker library to generate realistic test data
- **Environment-Aware**: Adapts data generation based on tenant settings
- **Type-Safe**: Returns properly typed model instances
- **Batch Creation**: Supports creating multiple instances at once
- **Tenant Customization**: Kansas-specific data generation for location-based testing

## Installation

The package is part of the test automation framework and requires the following dependencies:

```bash
pip install faker
```

## Quick Start

### Basic Usage

```python
from data_factory import create_player, create_credit_card, create_bank_account

# Create individual instances
player = create_player()
credit_card = create_credit_card()
bank_account = create_bank_account()

print(f"Player: {player.first_name} {player.last_name}")
print(f"Credit Card: {credit_card.card_number}")
print(f"Bank Account: {bank_account.account_number}")
```

### Batch Creation

```python
from data_factory import create_players, create_credit_cards

# Create multiple instances
players = create_players(count=5)
credit_cards = create_credit_cards(count=3)

print(f"Created {len(players)} players")
print(f"Created {len(credit_cards)} credit cards")
```

### Game Data Generation

```python
from data_factory import create_draw_game, create_instant_game

# Create game instances
draw_game = create_draw_game()
instant_game = create_instant_game()

print(f"Draw Game: {draw_game.game_name}")
print(f"Instant Game: {instant_game.game_name}")
```

## Available Factories

### Player Factory

- `create_player(**kwargs)` - Creates a single Player instance
- `create_players(count=1, **kwargs)` - Creates multiple Player instances

**Fields Generated:**
- first_name, last_name
- email (realistic format)
- date_of_birth
- phone_number
- address, city, state, zip_code
- latitude, longitude (Kansas-specific for Kansas tenant)

### Credit Card Factory

- `create_credit_card(**kwargs)` - Creates a single CreditCard instance
- `create_credit_cards(count=1, **kwargs)` - Creates multiple CreditCard instances

**Fields Generated:**
- card_number (realistic format)
- cardholder_name
- expiry_date
- cvv
- card_type (Visa, MasterCard, etc.)

### Bank Account Factory

- `create_bank_account(**kwargs)` - Creates a single BankAccount instance
- `create_bank_accounts(count=1, **kwargs)` - Creates multiple BankAccount instances

**Fields Generated:**
- account_number
- account_holder_name
- routing_number
- account_type (checking, savings)
- balance

### Draw Game Factory

- `create_draw_game(**kwargs)` - Creates a single DrawGame instance
- `create_draw_games(count=1, **kwargs)` - Creates multiple DrawGame instances

**Fields Generated:**
- game_name
- game_type (powerball, lottery, daily)
- draw_schedule
- ticket_price
- jackpot_amount

### Instant Game Factory

- `create_instant_game(**kwargs)` - Creates a single InstantGame instance
- `create_instant_games(count=1, **kwargs)` - Creates multiple InstantGame instances

**Fields Generated:**
- game_name
- ticket_price
- top_prize
- game_number
- launch_date

## Environment Integration

The factories are integrated with the environment package and will generate tenant-specific data:

### Kansas Tenant
- Generates Kansas-specific addresses and coordinates
- Uses Kansas cities and zip codes
- Consistent geographic data for location-based testing

### Default Tenant
- Uses general US-based data
- Standard Faker providers for all fields

## Customization

All factory functions accept keyword arguments to override specific fields:

```python
# Custom player with specific email
player = create_player(email="test@example.com")

# Custom credit card with specific type
card = create_credit_card(card_type="visa")

# Custom bank account with specific balance
account = create_bank_account(balance=1000.00)
```

## Testing

The package includes comprehensive tests to ensure data quality and consistency:

```bash
# Run all data factory tests
pytest data_factory/tests/ -v

# Run specific test
pytest data_factory/tests/test_data_factory.py::TestDataFactory::test_create_player -v
```

## Examples

See the `samples/` directory for practical examples:

- `basic_usage.py` - Basic factory usage examples
- `batch_creation.py` - Batch creation examples

## Integration with Models

The factories work seamlessly with the models package, returning properly typed instances:

```python
from data_factory import create_player
from models import Player

player = create_player()
assert isinstance(player, Player)
assert player.first_name is not None
assert "@" in player.email
```

## Logging

The package integrates with the logger package for debugging:

```python
from logger import log
from data_factory import create_player

log.set_level("DEBUG")
player = create_player()  # Will log debug information
```

## Error Handling

The factories include proper error handling and will raise appropriate exceptions for invalid parameters:

```python
try:
    players = create_players(count=-1)  # Invalid count
except ValueError as e:
    print(f"Error: {e}")
```

## Performance

The factories are optimized for test data generation:

- Efficient Faker instance management
- Minimal memory footprint
- Fast generation even for large batches
- Consistent seeding for reproducible results

## Package Structure

```
data_factory/
├── __init__.py                  # Package exports
├── player_factory.py           # Player data generation
├── credit_card_factory.py      # Credit card data generation
├── bank_account_factory.py     # Bank account data generation
├── draw_game_factory.py        # Draw game data generation
├── instant_game_factory.py     # Instant game data generation
├── samples/
│   ├── basic_usage.py          # Basic usage examples
│   └── batch_creation.py       # Batch creation examples
└── tests/
    └── test_data_factory.py    # Comprehensive test suite
```

## Dependencies

- `faker` - For realistic data generation
- `models` - For model type definitions
- `environment` - For tenant-specific configuration
- `logger` - For debug logging

## Contributing

When adding new factories:

1. Follow the existing naming convention (`create_*` and `create_*s`)
2. Add comprehensive tests
3. Update the `__init__.py` exports
4. Document the new factory in this README
5. Include tenant-specific customizations where applicable

## License

This package is part of the test automation framework and follows the same license terms.
