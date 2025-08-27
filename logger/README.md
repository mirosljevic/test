# Logger Framework 📝

Advanced logging system with colored output, structured logging, multi-level configuration, and comprehensive test execution monitoring.

## Overview

The logger framework provides sophisticated logging capabilities with colored console output, file logging, structured logging, and integration with the test automation framework for comprehensive monitoring and debugging.

## Key Features

- **Colored Console Output**: Color-coded log levels for better readability
- **Multi-Level Logging**: Debug, info, warning, error, and critical levels
- **Structured Logging**: JSON and structured format support
- **File and Console Output**: Simultaneous logging to multiple destinations
- **Test Integration**: Automatic test execution logging and reporting
- **Performance Monitoring**: Execution time and performance metrics
- **Log Filtering**: Advanced filtering and searching capabilities

## Quick Start

```python
from logger import log

log.info("Hello from the logger!")
log.warning("Something might be wrong.")
log.error("Something went wrong!")
log.debug("Debug information")
```

## Architecture

The logger package consists of:

- **`logger.py`**: Core logging logic with `Logger` class and `ColoredFormatter`
- **`colors.py`**: ANSI color definitions using `LogColor` enum
- **`__init__.py`**: Package initialization with global `log` instance
- **`settings/logger.py`**: Configuration management via environment variables

## Configuration

All configuration is managed through environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `LOGGER_LOG_LEVEL` | `DEBUG` | Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL) |
| `LOGGER_LOG_TO_FILE` | `False` | Enable file logging |
| `LOGGER_LOG_FILE_PATH` | `log/execution.log` | Log file path |
| `LOGGER_COLORIZE_OUTPUT` | `True` | Enable colorized console output |
| `LOGGER_DATE_FORMAT` | `%Y-%m-%d %H:%M:%S` | Date format for timestamps |
| `LOGGER_FORMAT` | `%(asctime)s - %(levelname)s - %(message)s` | Log message format |

## Usage Examples

### Basic Logging

```python
from logger import log

# Different log levels
log.debug("Debug information")
log.info("Information message")
log.warning("Warning message")
log.error("Error message")
log.critical("Critical error")

# Exception handling
try:
    result = 10 / 0
except ZeroDivisionError:
    log.exception("Division by zero occurred")
```

### Custom Logger Instance

```python
from logger.logger import Logger

# Create a custom logger for a specific module
custom_log = Logger("my_module")
custom_log.info("Custom logger message")
```

### Environment Variable Configuration

```bash
# Set log level to INFO
LOGGER_LOG_LEVEL=INFO python your_script.py

# Enable file logging
LOGGER_LOG_TO_FILE=true LOGGER_LOG_FILE_PATH=my_app.log python your_script.py

# Disable colors
LOGGER_COLORIZE_OUTPUT=false python your_script.py

# Custom format
LOGGER_FORMAT="[%(levelname)s] %(message)s" python your_script.py
```

## Color Scheme

The logger uses the following color scheme for different log levels:

- **DEBUG**: Light Grey (`\033[0;37m`)
- **INFO**: Green (`\033[0;32m`)
- **WARNING**: Yellow (`\033[0;33m`)
- **ERROR**: Red (`\033[0;31m`)
- **CRITICAL**: Magenta (`\033[0;35m`)

## Available Colors

The `LogColor` enum provides these ANSI color codes:

- Basic colors: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
- Grey variants: DARK_GREY, LIGHT_GREY
- Bright colors: BRIGHT_BLACK, BRIGHT_RED, BRIGHT_GREEN, etc.
- RESET: Resets formatting


## Running Examples

```bash
# Basic usage example
python logger/samples/basic_usage.py

# With custom log level
LOGGER_LOG_LEVEL=INFO python logger/samples/basic_usage.py

# With file logging enabled
LOGGER_LOG_TO_FILE=true python logger/samples/file_logging.py

# With colors disabled
LOGGER_COLORIZE_OUTPUT=false python logger/samples/basic_usage.py

# Custom logger example
python logger/samples/custom_logger.py
```

## Testing

Run the test suite to verify functionality:

```bash
# Run logger tests
python -m pytest logger/tests/ -v

# Run specific test file
python -m pytest logger/tests/test_logger.py -v

# Run with coverage (if pytest-cov is installed)
python -m pytest logger/tests/ --cov=logger --cov-report=html
```
