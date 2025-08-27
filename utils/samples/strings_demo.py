from utils.strings import sanitize_filename, truncate_string, snake_to_camel, camel_to_snake

print("String Utilities Demo")
print("=" * 30)

print("Filename sanitization:")
filenames = [
    "test<file>.txt",
    "data/report.pdf",
    "user:input.log",
    "file*with?chars.txt",
    "   .hidden   "
]

for filename in filenames:
    sanitized = sanitize_filename(filename)
    print(f"'{filename}' -> '{sanitized}'")

print("\nString truncation:")
text = "This is a very long string that needs to be truncated"
print(f"Original: '{text}'")
print(f"Truncated (20): '{truncate_string(text, 20)}'")
print(f"Truncated (30, '...'): '{truncate_string(text, 30, '...')}'")
print(f"Truncated (25, '[more]'): '{truncate_string(text, 25, '[more]')}'")

print("\nCase conversion:")
snake_cases = ["user_name", "api_key", "database_connection"]
camel_cases = ["userName", "apiKey", "databaseConnection"]

print("Snake to Camel:")
for snake in snake_cases:
    camel = snake_to_camel(snake)
    print(f"'{snake}' -> '{camel}'")

print("\nCamel to Snake:")
for camel in camel_cases:
    snake = camel_to_snake(camel)
    print(f"'{camel}' -> '{snake}'")
