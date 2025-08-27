import pytest
from datetime import datetime, timezone
from utils.datetime import get_current_timestamp, format_duration, parse_iso_timestamp


class TestDateTimeUtils:

    def test_get_current_timestamp_returns_iso_format(self):
        timestamp = get_current_timestamp()
        assert isinstance(timestamp, str)
        assert "T" in timestamp
        assert timestamp.endswith("+00:00") or timestamp.endswith("Z")

    def test_format_duration_seconds_only(self):
        assert format_duration(5.5) == "5.5s"
        assert format_duration(30.0) == "30.0s"

    def test_format_duration_minutes_and_seconds(self):
        assert format_duration(75.3) == "1m 15.3s"
        assert format_duration(120.0) == "2m"

    def test_format_duration_hours_minutes_seconds(self):
        assert format_duration(3665.8) == "1h 1m 5.8s"
        assert format_duration(7200.0) == "2h"

    def test_parse_iso_timestamp_valid_formats(self):
        result = parse_iso_timestamp("2024-07-15T10:30:00Z")
        assert isinstance(result, datetime)
        assert result.year == 2024
        assert result.month == 7
        assert result.day == 15

        result = parse_iso_timestamp("2024-07-15T10:30:00+00:00")
        assert isinstance(result, datetime)

    def test_parse_iso_timestamp_invalid_format(self):
        result = parse_iso_timestamp("invalid-timestamp")
        assert result is None

        result = parse_iso_timestamp("")
        assert result is None

    def test_parse_iso_timestamp_with_microseconds(self):
        result = parse_iso_timestamp("2024-07-15T10:30:00.123456Z")
        assert isinstance(result, datetime)
        assert result.microsecond == 123456
