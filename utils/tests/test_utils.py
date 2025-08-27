import pytest
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


class TestUtilsPackage:

    def test_imports_available(self):
        assert callable(get_config_var)
        assert callable(sanitize_filename)
        assert callable(truncate_string)
        assert callable(snake_to_camel)
        assert callable(camel_to_snake)
        assert callable(get_current_timestamp)
        assert callable(format_duration)
        assert callable(parse_iso_timestamp)

    def test_config_functionality(self):
        result = get_config_var("NONEXISTENT_VAR", "default")
        assert result == "default"

    def test_string_functionality(self):
        result = sanitize_filename("test<file>.txt")
        assert result == "test_file_.txt"

    def test_datetime_functionality(self):
        timestamp = get_current_timestamp()
        assert isinstance(timestamp, str)
        assert "T" in timestamp
