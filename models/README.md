# Models Package

A comprehensive collection of data models for the test automation framework, providing strongly-typed representations of business entities used in lottery and gaming applications.

## Features

- **Dataclass-based Models**: Clean, type-safe data structures using Python dataclasses
- **Enum Support**: Strongly-typed enumerations for game types, roles, and bonus types
- **Validation**: Built-in data validation and business logic
- **String Representations**: Human-readable string representations for all models
- **Property Methods**: Computed properties for derived data
- **MongoDB Compatibility**: Serialization support for database operations
- **Comprehensive Coverage**: Models for players, operators, games, payments, and bonuses

## Quick Start

```python
from models import Player, Operator, OperatorRole, InstantGame, GameType

# Create a player
player = Player(
    first_name="John",
    last_name="Doe",
    email="john.doe@example.com"
)

# Create an operator
operator = Operator(
    username="risk_analyst_1",
    password="secure_password",
    role=OperatorRole.RISK_ANALYST
)

# Create a game
game = InstantGame(
    game_type=GameType.PRIMETIME_PAYOUT,
    game_id="PRIMETIME001"
)
```

## Available Models

### **Core Entity Models**

#### **Player Model**
Represents a player/customer in the system.

```python
from models import Player

player = Player(
    first_name="Jane",
    last_name="Smith",
    email="jane.smith@example.com",
    date_of_birth=datetime(1990, 5, 15),
    geolocation=(40.7128, -74.0060)  # NYC coordinates
)

print(player.full_name)  # "Jane Smith"
print(player.age)        # Calculated age
print(player.location_string)  # Formatted coordinates
```

**Key Properties:**
- `full_name`: Computed full name
- `age`: Calculated age from date of birth
- `account_age`: Days since registration
- `location_string`: Formatted geolocation
- `latitude`/`longitude`: Individual coordinate access

#### **Operator Model**
Represents system operators with specific roles.

```python
from models import Operator, OperatorRole

operator = Operator(
    username="analyst_001",
    password="secure_pass",
    role=OperatorRole.RISK_ANALYST
)

print(operator)  # "analyst_001 (Risk Analyst)"
```

**Available Roles:**
- `RISK_ANALYST`: Risk analysis operations
- `MARKETING_ANALYST`: Marketing and promotional operations

### **Game Models**

#### **InstantGame Model**
Represents instant/scratch games.

```python
from models import InstantGame, GameType

game = InstantGame(
    game_type=GameType.PRIMETIME_PAYOUT,
    game_id="PRIME001",
    enabled=True,
    ticket_price=5.00
)
```

**Available Game Types:**
- `PRIMETIME_PAYOUT`: Primetime Payout game
- `TRITONS_TREASURES`: Triton's Treasures game
- `RICHCRAFT`: Richcraft game
- `CAULDRON_ME_CRAZY`: Cauldron Me Crazy game
- `HOLIDAY_VIP_RICHES`: Holiday VIP Riches game
- `HAND_TO_HAND_TACTICS`: Hand to Hand Tactics game

#### **DrawGame Model**
Represents draw-based lottery games.

```python
from models import DrawGame, DrawGameType

draw_game = DrawGame(
    game_type=DrawGameType.POWERBALL,
    draw_id="PB20240101",
    ticket_price=2.00
)
```

**Available Draw Game Types:**
- `POWERBALL`: Multi-state Powerball lottery
- `MEGA_MILLIONS`: Multi-state Mega Millions lottery
- `PICK_3`: Pick 3 daily draw game
- `PICK_4`: Pick 4 daily draw game

### **Payment Models**

#### **CreditCard Model**
Represents credit card payment methods.

```python
from models import CreditCard

card = CreditCard(
    number="4111111111111111",
    expiry_month="12",
    expiry_year="2025",
    cvv="123",
    cardholder_name="John Doe"
)

print(card.masked_number)    # "****1111"
print(card.detect_card_type())  # "Visa"
```

**Features:**
- Automatic card type detection (Visa, MasterCard, Amex, Discover)
- Number masking for security
- Validation support

#### **BankAccount Model**
Represents bank account payment methods.

```python
from models import BankAccount

account = BankAccount(
    account_number="1234567890",
    routing_number="021000021",
    account_type="CHECKING",
    account_holder_name="Jane Doe"
)

print(account.masked_account_number)  # "****7890"
print(account.masked_routing_number)  # "****0021"
```

### **Bonus Models**

#### **Bonus Model**
Represents promotional bonuses and offers.

```python
from models import Bonus, BonusType

bonus = Bonus(
    bonus_type=BonusType.FREE_ROUNDS,
    status="ACTIVE",
    number_of_rounds=10,
    allowed_games=["PRIMETIME", "RICHCRAFT"]
)
```

**Available Bonus Types:**
- `FREE_ROUNDS`: Free game rounds
- `PLAY_CREDIT`: Play credit bonuses
- `CASH_CREDIT`: Cash credit bonuses
- `FUNDS_MATCHUP`: Deposit matching bonuses

## Architecture

The models package follows these design principles:

### **Dataclass Pattern**
All models use Python dataclasses for:
- Automatic `__init__` method generation
- Type hints and validation
- Clean, readable code structure
- Built-in equality and representation methods

### **Enum-based Type Safety**
Enumerations provide:
- Strongly-typed constants
- Controlled vocabularies
- IDE autocompletion support
- Runtime validation

### **Property Methods**
Computed properties for:
- Derived data calculations
- Formatting and display
- Data transformation
- Validation checks

### **MongoDB Integration**
Models support database operations through:
- Custom `to_dict` methods for serialization
- Enum value conversion
- Type-safe field mapping


## Usage Examples

### **Player Management**

```python
from models import Player
from datetime import datetime

# Create a new player
player = Player(
    first_name="Alice",
    last_name="Johnson",
    email="alice.johnson@example.com",
    date_of_birth=datetime(1985, 3, 20),
    phone="+1-555-0123",
    address="123 Main St",
    city="Springfield",
    state="IL",
    zip_code="62701",
    country="USA",
    geolocation=(39.7817, -89.6501)
)

# Access computed properties
print(f"Player: {player.full_name}")
print(f"Age: {player.age} years")
print(f"Location: {player.location_string}")
print(f"Coordinates: {player.latitude}, {player.longitude}")
```

### **Game Configuration**

```python
from models import InstantGame, DrawGame, GameType, DrawGameType

# Configure instant games
instant_games = [
    InstantGame(
        game_type=GameType.PRIMETIME_PAYOUT,
        game_id="PRIME001",
        enabled=True,
        ticket_price=5.00
    ),
    InstantGame(
        game_type=GameType.RICHCRAFT,
        game_id="RICH001", 
        enabled=True,
        ticket_price=2.00
    )
]

# Configure draw games
draw_games = [
    DrawGame(
        game_type=DrawGameType.POWERBALL,
        draw_id="PB20240101",
        ticket_price=2.00
    ),
    DrawGame(
        game_type=DrawGameType.MEGA_MILLIONS,
        draw_id="MM20240101",
        ticket_price=2.00
    )
]
```

### **Payment Method Setup**

```python
from models import CreditCard, BankAccount

# Credit card setup
credit_card = CreditCard(
    number="4111111111111111",
    expiry_month="12",
    expiry_year="2025",
    cvv="123",
    cardholder_name="John Smith"
)

# Bank account setup
bank_account = BankAccount(
    account_number="1234567890",
    routing_number="021000021",
    account_type="CHECKING",
    account_holder_name="John Smith"
)

# Payment methods with security
print(f"Card: {credit_card.masked_number} ({credit_card.detect_card_type()})")
print(f"Account: {bank_account.masked_account_number}")
```

### **Bonus Management**

```python
from models import Bonus, BonusType

# Create different bonus types
bonuses = [
    Bonus(
        bonus_type=BonusType.FREE_ROUNDS,
        status="ACTIVE",
        number_of_rounds=10,
        allowed_games=["PRIMETIME", "RICHCRAFT"]
    ),
    Bonus(
        bonus_type=BonusType.PLAY_CREDIT,
        status="PENDING",
        total_amount=25.00,
        amount_type="FIXED"
    ),
    Bonus(
        bonus_type=BonusType.FUNDS_MATCHUP,
        status="ACTIVE",
        total_amount=100.00,
        amount_type="PERCENTAGE"
    )
]
```

## Running Examples

```bash
# Player model examples
python models/samples/create_player.py

# Operator model examples
python models/samples/operator.py

# Game model examples
python models/samples/instant_game.py
python models/samples/draw_game.py

# Payment model examples
python models/samples/credit_card.py
python models/samples/bank_account.py

# Bonus model examples
python models/samples/bonus.py
```

## Testing

Run the comprehensive test suite:

```bash
# Run all model tests
python -m pytest models/tests/ -v

# Run specific model tests
python -m pytest models/tests/test_player.py -v
python -m pytest models/tests/test_operator.py -v
python -m pytest models/tests/test_instant_game.py -v

# Run with coverage
python -m pytest models/tests/ --cov=models --cov-report=html
```

## Integration with Framework

### **Database Integration**

Models integrate seamlessly with MongoDB clients:

```python
from models import Player
from mongo import PlayerMongoClient

# Create player and save to database
player = Player(first_name="Test", last_name="User")
player_client = PlayerMongoClient(player=player)
player_client.insert()
```

### **API Integration**

Models work with API clients:

```python
from models import Operator, OperatorRole
from api.clients.operator_client import OperatorApiClient

# Create operator and use with API
operator = Operator(
    username="analyst1",
    password="pass123",
    role=OperatorRole.RISK_ANALYST
)
api_client = OperatorApiClient(operator=operator)
```

### **Data Factory Integration**

Models are used by data factories:

```python
from data_factory import create_player
from models import Player

# Factory creates properly structured Player models
player = create_player()
assert isinstance(player, Player)
```

## Validation and Business Logic

### **Player Validation**
- Email format validation
- Age requirements (18+ years)
- Geolocation coordinate validation
- Required field checks

### **Payment Validation**
- Credit card number format
- Card type detection
- Account number masking
- Security field handling

### **Game Validation**
- Game type consistency
- Price validation
- Status checking
- Configuration validation

## Best Practices

### **Model Creation**
```python
# Use keyword arguments for clarity
player = Player(
    first_name="John",
    last_name="Doe",
    email="john@example.com"
)

# Not recommended
player = Player("John", "Doe", "john@example.com")
```

### **Enum Usage**
```python
# Use enum constants
role = OperatorRole.RISK_ANALYST

# Not string literals
role = "RISK_ANALYST"  # Avoid this
```

### **Property Access**
```python
# Use computed properties
full_name = player.full_name
age = player.age

# Instead of manual calculation
full_name = f"{player.first_name} {player.last_name}"
```
