import pytest
from unittest.mock import patch, MagicMock
from utils.config import get_config_var
from utils.strings import sanitize_filename, truncate_string, snake_to_camel, camel_to_snake
from utils.datetime import get_current_timestamp, format_duration, parse_iso_timestamp
from datetime import datetime, timezone


class TestConfigUtils:

    def test_get_config_var_with_default(self):
        result = get_config_var("NON_EXISTENT_VAR", "default_value")
        assert result == "default_value"

    @patch.dict('os.environ', {'TEST_BOOL': 'true'})
    def test_get_config_var_boolean_true(self):
        result = get_config_var("TEST_BOOL", False)
        assert result is True

    @patch.dict('os.environ', {'TEST_BOOL': 'false'})
    def test_get_config_var_boolean_false(self):
        result = get_config_var("TEST_BOOL", True)
        assert result is False

    @patch.dict('os.environ', {'TEST_INT': '42'})
    def test_get_config_var_integer(self):
        result = get_config_var("TEST_INT", 0)
        assert result == 42

    @patch.dict('os.environ', {'TEST_FLOAT': '3.14'})
    def test_get_config_var_float(self):
        result = get_config_var("TEST_FLOAT", 0.0)
        assert result == 3.14

    @patch.dict('os.environ', {'TEST_STRING': 'hello'})
    def test_get_config_var_string(self):
        result = get_config_var("TEST_STRING", "default")
        assert result == "hello"


class TestStringUtils:

    def test_sanitize_filename_basic(self):
        result = sanitize_filename("test<file>.txt")
        assert result == "test_file_.txt"

    def test_sanitize_filename_empty(self):
        result = sanitize_filename("")
        assert result == "unnamed"

    def test_sanitize_filename_whitespace(self):
        result = sanitize_filename("   .hidden   ")
        assert result == "hidden"

    def test_truncate_string_no_truncation(self):
        result = truncate_string("short", 10)
        assert result == "short"

    def test_truncate_string_with_truncation(self):
        result = truncate_string("very long string", 10)
        assert result == "very lo..."

    def test_truncate_string_custom_suffix(self):
        result = truncate_string("long text", 8, "[more]")
        assert result == "lo[more]"

    def test_snake_to_camel_basic(self):
        result = snake_to_camel("user_name")
        assert result == "userName"

    def test_snake_to_camel_single_word(self):
        result = snake_to_camel("user")
        assert result == "user"

    def test_camel_to_snake_basic(self):
        result = camel_to_snake("userName")
        assert result == "user_name"

    def test_camel_to_snake_single_word(self):
        result = camel_to_snake("user")
        assert result == "user"


class TestDateTimeUtils:

    def test_get_current_timestamp(self):
        result = get_current_timestamp()
        assert isinstance(result, str)
        assert "T" in result
        assert result.endswith("+00:00")

    def test_format_duration_seconds(self):
        result = format_duration(5.5)
        assert result == "5.5s"

    def test_format_duration_minutes(self):
        result = format_duration(75.3)
        assert result == "1m 15.3s"

    def test_format_duration_hours(self):
        result = format_duration(3665.8)
        assert result == "1h 1m 5.8s"

    def test_format_duration_exact_minutes(self):
        result = format_duration(120)
        assert result == "2m"

    def test_parse_iso_timestamp_valid(self):
        result = parse_iso_timestamp("2024-07-15T10:30:00Z")
        assert isinstance(result, datetime)
        assert result.year == 2024
        assert result.month == 7
        assert result.day == 15

    def test_parse_iso_timestamp_invalid(self):
        result = parse_iso_timestamp("invalid-timestamp")
        assert result is None

    def test_parse_iso_timestamp_with_timezone(self):
        result = parse_iso_timestamp("2024-07-15T10:30:00+00:00")
        assert isinstance(result, datetime)
        assert result.year == 2024
