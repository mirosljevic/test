import pytest
from logger import log
from logger.logger import Logger
from logger.colors import LogColor


class TestLogger:
    def test_basic_logging(self):
        assert log is not None
        assert hasattr(log, "info")
        assert hasattr(log, "error")
        assert hasattr(log, "warning")

        log.info("Test info message")
        log.error("Test error message")
        log.warning("Test warning message")

    def test_custom_logger(self):
        custom_logger = Logger("test_logger")
        assert custom_logger.custom_logger is not None
        assert custom_logger.custom_logger.name == "test_logger"

        custom_logger.info("Custom logger test")

    def test_log_colors(self):
        assert hasattr(LogColor, "RED")
        assert hasattr(LogColor, "GREEN")
        assert hasattr(LogColor, "YELLOW")
        assert isinstance(LogColor.RED.value, str)

    def test_exception_logging(self):
        try:
            raise ValueError("Test exception")
        except ValueError:
            log.exception("Exception occurred during test")

        assert hasattr(log, "exception")


if __name__ == "__main__":
    pytest.main([__file__])
