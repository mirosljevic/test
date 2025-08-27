# Test Automation Framework 🚀

A comprehensive multi-platform test automation framework supporting web, mobile, and API testing with advanced device detection and real-time monitoring capabilities.

## 📋 Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Project Structure](#project-structure)
- [Framework Components](#framework-components)
- [Device Support](#device-support)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)

## ✨ Features

- **Multi-Platform Testing**: Web, Mobile, API testing in unified framework
- **Advanced Device Detection**: Mobile, Tablet, Desktop layout-aware testing
- **Real-time Dashboard**: Live test monitoring and analytics
- **Multi-Tenant Support**: Kansas and other tenant configurations
- **Flexible Page Object Model**: Enhanced component-based architecture
- **Email Testing**: Automated email verification and testing
- **Database Integration**: PostgreSQL and MongoDB support
- **CI/CD Ready**: Jenkins integration and containerized execution
- **Comprehensive Reporting**: HTML, JSON, and real-time reporting

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Node.js (for Playwright)
- PostgreSQL (optional)
- MongoDB (optional)

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd test_auto

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Basic Usage

```bash
# Run all tests
pytest

# Run with specific device
DEVICE=ipad_air pytest tests/ui/

# Run with dashboard monitoring
PYTHONPATH=. pytest --tb=short -p dashboard.pytest_plugin

# Run API tests only
pytest tests/api/
```

## 📁 Project Structure

```
test_auto/
├── 📄 README.md                 # This file
├── ⚙️ pytest.ini                # Pytest configuration
├── 📦 requirements.txt          # Python dependencies
│
├── 🎭 actors/                   # Test actors and personas
│   ├── 📄 README.md
│   ├── 📜 __init__.py
│   ├── 🎯 base.py              # Base actor functionality
│   ├── 👤 player.py            # Player actor implementation
│   └── 🔧 operator.py          # Operator actor implementation
│
├── 🌐 api/                      # API testing framework
│   ├── 📄 README.md
│   ├── 📜 __init__.py
│   ├── 🔌 clients/             # API clients
│   ├── 🛣️ endpoints/           # Endpoint definitions
│   └── ⚡ executor/            # Test execution engine
│
├── 🖥️ ui/                       # UI testing framework
│   ├── 📄 README.md
│   ├── 📜 __init__.py
│   ├── 🏛️ facade/              # UI facades and features
│   ├── 📄 pages/               # Page objects
│   └── 📱 samples/             # UI test samples
│
├── 📊 dashboard/                # Real-time monitoring (POC)
│   └── 📄 README.md
│
├── 🏗️ data_factory/            # Test data generation
│   ├── 📄 README.md
│   ├── 🏭 factories/           # Data factories
│   └── 📋 samples/             # Sample data
│
├── 🗄️ database/                # Database utilities
│   ├── 📄 README.md
│   ├── 🐘 postgres.py          # PostgreSQL integration
│   └── 📋 samples/             # Database samples
│
├── 📧 email_service/            # Email testing utilities
│   ├── 📄 README.md
│   ├── 📬 base.py              # Base email client
│   ├── 🐕 mailhog/             # MailHog integration
│   └── ⏰ temp_mail/           # Temporary email service
│
├── 🌍 environment/              # Environment management
│   ├── 📄 README.md
│   ├── ⚙️ loader.py            # Environment loader
│   └── 🏢 envs/                # Environment configs
│
├── 📋 logger/                   # Logging utilities
│   ├── 📄 README.md
│   ├── 🎨 colors.py            # Console colors
│   └── 📝 logger.py            # Logger implementation
│
├── 📱 mobile/                   # Mobile testing utilities
│   ├── 📄 README.md
│   ├── ⚙️ config.py            # Mobile configuration
│   └── 📱 clients/             # Mobile clients
│
├── 🏗️ models/                  # Data models
│   ├── 📄 README.md
│   ├── 👤 player.py            # Player model
│   ├── 🎰 bonus.py             # Bonus model
│   └── 💳 credit_card.py       # Payment models
│
├── 🗄️ mongo/                   # MongoDB utilities
│   ├── 📄 README.md
│   ├── 🔌 base_client.py       # Base MongoDB client
│   └── 📋 samples/             # MongoDB samples
│
├── ⚙️ settings/                # Framework settings
│   ├── 📄 README.md
│   ├── 🌍 environment.py       # Environment settings
│   ├── 🖥️ devices.py           # Device configurations
│   └── 📝 logger.py            # Logger settings
│
├── 🧪 tests/                   # Test suites
│   ├── 📄 README.md
│   ├── 🌐 ui/                  # UI tests
│   ├── 🔌 api/                 # API tests
│   └── 📱 mobile/              # Mobile tests
│
└── 🔧 utils/                   # Utility functions
    ├── 📄 README.md
    ├── ⚙️ config.py            # Configuration utilities
    ├── 📅 datetime.py          # Date/time utilities
    └── 🍲 soup.py              # Web scraping utilities
```

## 🧩 Framework Components

### [🎭 Actors](actors/README.md)
Test personas representing different user types (Player, Operator) with role-specific capabilities and data generation.

### [🌐 API Testing](api/README.md)
Comprehensive API testing framework with client libraries, endpoint definitions, and automated validation.

### [🖥️ UI Testing](ui/README.md)
Advanced UI testing with device-aware page objects, layout detection, and cross-platform compatibility.

### [📊 Dashboard](dashboard/README.md)
Real-time test monitoring with live updates, device analytics, and session management.

### [🏗️ Data Factory](data_factory/README.md)
Automated test data generation with factories for players, games, transactions, and more.

### [🗄️ Database](database/README.md)
Database testing utilities supporting PostgreSQL and MongoDB with sample data and migrations.

### [📧 Email Service](email_service/README.md)
Email testing capabilities with MailHog, temporary email services, and verification workflows.

### [🌍 Environment](environment/README.md)
Multi-environment configuration management for different testing stages and tenants.

### [📋 Logger](logger/README.md)
Enhanced logging with colors, structured output, and integration with test reporting.

### [📱 Mobile](mobile/README.md)
Mobile testing utilities with device configurations and mobile-specific test helpers.

### [🏗️ Models](models/README.md)
Data models representing business entities like players, bonuses, payments, and games.

### [🗄️ MongoDB](mongo/README.md)
MongoDB integration with specialized clients for players, operators, and game data.

### [⚙️ Settings](settings/README.md)
Framework configuration including device settings, environment variables, and logging configuration.

### [🧪 Tests](tests/README.md)
Test suites organized by platform (UI, API, Mobile) with examples and best practices.

### [🔧 Utils](utils/README.md)
Common utility functions for configuration, date/time handling, web scraping, and more.

## 📱 Device Support

The framework supports comprehensive device testing with automatic layout detection:

### Desktop Browsers
- Chrome, Firefox, Safari, Edge
- Multiple viewport sizes
- Desktop-specific UI patterns

### Mobile Devices
- iPhone 12, iPhone 13, iPhone 14
- Samsung Galaxy devices
- Mobile-first UI patterns
- Touch interactions

### Tablet Devices
- iPad Air, iPad Pro
- Samsung Galaxy Tab
- Hybrid UI patterns (mobile + desktop)
- Adaptive layout detection

### Configuration
```bash
# Set device for testing
DEVICE=ipad_air pytest tests/ui/

# Available devices
DEVICE=desktop|ipad_pro|ipad_air|iphone_12|samsung_galaxy_tab
```

## ⚙️ Configuration

### Environment Variables
```bash
# Core settings
ENVIRONMENT=pgp_sit|pgp_prod|catalyst_sit
TENANT=kansas|catalyst
DEVICE=desktop|mobile|tablet

# Database
DATABASE_URL=postgresql://user:pass@localhost/db
MONGO_URL=mongodb://localhost:27017

# Email testing
EMAIL_SERVICE=mailhog|tempmail
MAILHOG_URL=http://localhost:8025

# Dashboard
DASHBOARD_URL=http://localhost:8000
```

### Device Configuration
```python
# Custom device settings
from settings.devices import DEVICES

# Available configurations in settings/devices.py
```

## 💡 Usage Examples

### Basic UI Test
```python
def test_player_registration(visitor):
    """Test player registration across different devices."""
    visitor.ui.open()
    result = visitor.ui.registration.register()
    assert result.success
    assert "Welcome" in result.message
```

### API Test with Database Validation
```python
def test_create_player_api(api_client, database):
    """Test player creation via API with database validation."""
    player_data = PlayerFactory.build()
    response = api_client.players.create(player_data)
    
    assert response.status_code == 201
    
    # Validate in database
    player = database.players.find_by_email(player_data.email)
    assert player.status == "active"
```

### Multi-Device Test
```python
@pytest.mark.parametrize("device", ["desktop", "ipad_air", "iphone_12"])
def test_login_across_devices(visitor, device):
    """Test login functionality across different devices."""
    os.environ['DEVICE'] = device
    
    visitor.ui.open()
    result = visitor.ui.authentication.login()
    assert result.success
```

## 🛠️ Development

### Running Tests Locally
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test categories
pytest -m "not slow"  # Skip slow tests
pytest -m "api"       # API tests only
pytest -m "ui"        # UI tests only
```

### Adding New Components

1. Create component directory with `README.md`
2. Add to main project structure documentation
3. Include tests in `tests/` directory
4. Update requirements.txt if new dependencies added

### Code Standards
- Follow PEP 8 for Python code
- Use type hints where possible
- Include docstrings for public methods
- Write comprehensive tests for new features

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:
- Check component-specific README files
- Review test examples in the `tests/` directory
- Check the [CHANGELOG.md](CHANGELOG.md) for recent updates

---

**Happy Testing!** 🎉