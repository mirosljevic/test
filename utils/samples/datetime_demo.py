import time
from utils.datetime import get_current_timestamp, format_duration, parse_iso_timestamp

print("DateTime Utilities Demo")
print("=" * 30)

print("Current timestamp:")
timestamp = get_current_timestamp()
print(f"Current time (UTC): {timestamp}")

print("\nDuration formatting:")
durations = [5.5, 75.3, 3665.8, 7325.2]
for duration in durations:
    formatted = format_duration(duration)
    print(f"{duration} seconds -> {formatted}")

print("\nISO timestamp parsing:")
timestamps = [
    "2024-07-15T10:30:00Z",
    "2024-07-15T10:30:00+00:00",
    "2024-07-15T10:30:00.123456Z",
    "invalid-timestamp"
]

for ts in timestamps:
    parsed = parse_iso_timestamp(ts)
    if parsed:
        print(f"'{ts}' -> {parsed}")
    else:
        print(f"'{ts}' -> Failed to parse")

print("\nPractical example:")
start_time = time.time()
time.sleep(0.1)
end_time = time.time()
elapsed = end_time - start_time
print(f"Operation took: {format_duration(elapsed)}")

print(f"\nCurrent operation timestamp: {get_current_timestamp()}")
