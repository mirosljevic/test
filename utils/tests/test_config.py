import pytest
from unittest.mock import patch
from utils.config import get_config_var


class TestConfigUtils:

    def test_get_config_var_returns_default_when_env_not_set(self):
        with patch.dict("os.environ", {}, clear=True):
            result = get_config_var("TEST_VAR", "default_value")
            assert result == "default_value"

    def test_get_config_var_returns_env_value_as_string(self):
        with patch.dict("os.environ", {"TEST_VAR": "env_value"}):
            result = get_config_var("TEST_VAR", "default_value")
            assert result == "env_value"

    def test_get_config_var_boolean_conversion(self):
        with patch.dict("os.environ", {"TEST_BOOL": "true"}):
            result = get_config_var("TEST_BOOL", False)
            assert result is True

        with patch.dict("os.environ", {"TEST_BOOL": "false"}):
            result = get_config_var("TEST_BOOL", True)
            assert result is False

        with patch.dict("os.environ", {"TEST_BOOL": "1"}):
            result = get_config_var("TEST_BOOL", False)
            assert result is True

    def test_get_config_var_integer_conversion(self):
        with patch.dict("os.environ", {"TEST_INT": "42"}):
            result = get_config_var("TEST_INT", 0)
            assert result == 42

        with patch.dict("os.environ", {"TEST_INT": "invalid"}):
            result = get_config_var("TEST_INT", 10)
            assert result == 10

    def test_get_config_var_float_conversion(self):
        with patch.dict("os.environ", {"TEST_FLOAT": "3.14"}):
            result = get_config_var("TEST_FLOAT", 0.0)
            assert result == 3.14

        with patch.dict("os.environ", {"TEST_FLOAT": "invalid"}):
            result = get_config_var("TEST_FLOAT", 1.5)
            assert result == 1.5
