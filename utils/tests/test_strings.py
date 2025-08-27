import pytest
from utils.strings import sanitize_filename, truncate_string, snake_to_camel, camel_to_snake


class TestStringUtils:

    def test_sanitize_filename_removes_invalid_characters(self):
        assert sanitize_filename("test<file>.txt") == "test_file_.txt"
        assert sanitize_filename("data/report.pdf") == "data_report.pdf"
        assert sanitize_filename("user:input.log") == "user_input.log"

    def test_sanitize_filename_handles_empty_result(self):
        assert sanitize_filename("") == "unnamed"
        assert sanitize_filename("   ") == "unnamed"
        assert sanitize_filename("...") == "unnamed"

    def test_truncate_string_no_truncation_needed(self):
        text = "Short text"
        assert truncate_string(text, 20) == "Short text"

    def test_truncate_string_with_truncation(self):
        text = "This is a very long string"
        result = truncate_string(text, 10)
        assert result == "This is..."
        assert len(result) == 10

    def test_truncate_string_custom_suffix(self):
        text = "Long text here"
        result = truncate_string(text, 10, "[more]")
        assert result == "Long[more]"
        assert len(result) == 10

    def test_snake_to_camel_conversion(self):
        assert snake_to_camel("user_name") == "userName"
        assert snake_to_camel("api_key") == "apiKey"
        assert snake_to_camel("simple") == "simple"

    def test_camel_to_snake_conversion(self):
        assert camel_to_snake("userName") == "user_name"
        assert camel_to_snake("apiKey") == "api_key"
        assert camel_to_snake("simple") == "simple"

    def test_snake_camel_roundtrip(self):
        original = "test_variable_name"
        camel = snake_to_camel(original)
        back_to_snake = camel_to_snake(camel)
        assert back_to_snake == original
