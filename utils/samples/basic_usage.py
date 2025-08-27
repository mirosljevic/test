from utils import (
    get_config_var,
    sanitize_filename,
    truncate_string,
    snake_to_camel,
    camel_to_snake,
    get_current_timestamp,
    format_duration,
    parse_iso_timestamp
)

print("Utils Package Demo")
print("=" * 30)

print("Config:")
debug_mode = get_config_var("DEBUG_MODE", False)
print(f"Debug mode: {debug_mode}")

print("\nString utilities:")
filename = sanitize_filename("test<file>.txt")
print(f"Sanitized filename: {filename}")

truncated = truncate_string("Long text example", 10)
print(f"Truncated text: {truncated}")

camel = snake_to_camel("user_name")
print(f"Snake to camel: {camel}")

snake = camel_to_snake("userName")
print(f"Camel to snake: {snake}")

print("\nDateTime utilities:")
timestamp = get_current_timestamp()
print(f"Current timestamp: {timestamp}")

duration = format_duration(125.5)
print(f"Formatted duration: {duration}")

parsed = parse_iso_timestamp("2024-07-15T10:30:00Z")
print(f"Parsed timestamp: {parsed}")

print("\nUtils package ready for use!")
