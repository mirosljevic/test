import logging
import sys
from typing import Optional

from .colors import LogColor
from settings.logger import (
    LOGGER_LOG_LEVEL,
    LOGGER_LOG_TO_FILE,
    LOGGER_LOG_FILE_PATH,
    LOGGER_COLORIZE_OUTPUT,
    LOGGER_DATE_FORMAT,
    LOGGER_FORMAT,
)


class ColoredFormatter(logging.Formatter):
    LEVEL_COLORS = {
        logging.DEBUG: LogColor.LIGHT_GREY,
        logging.INFO: LogColor.GREEN,
        logging.WARNING: LogColor.YELLOW,
        logging.ERROR: LogColor.RED,
        logging.CRITICAL: LogColor.MAGENTA,
    }

    def __init__(
            self,
            fmt: str,
            date_fmt: Optional[str] = None,
            colorize: bool = True):
        super().__init__(fmt, date_fmt)
        self.colorize = colorize

    def format(self, record: logging.LogRecord) -> str:
        if not self.colorize:
            return super().format(record)

        color = self.LEVEL_COLORS.get(record.levelno, LogColor.WHITE)
        formatted_message = super().format(record)
        return f"{color.value}{formatted_message}{LogColor.RESET.value}"


class Logger:
    def __init__(self, name: str = "app"):
        self.custom_logger = logging.getLogger(name)
        self.custom_logger.setLevel(getattr(logging, LOGGER_LOG_LEVEL.upper()))

        self.custom_logger.handlers.clear()
        self._setup_console_handler()

        if LOGGER_LOG_TO_FILE:
            self._setup_file_handler()

    def _setup_console_handler(self):
        console_handler = logging.StreamHandler(sys.stdout)
        console_formatter = ColoredFormatter(
            LOGGER_FORMAT, LOGGER_DATE_FORMAT, LOGGER_COLORIZE_OUTPUT
        )
        console_handler.setFormatter(console_formatter)
        self.custom_logger.addHandler(console_handler)

    def _setup_file_handler(self):
        file_handler = logging.FileHandler(LOGGER_LOG_FILE_PATH)
        file_formatter = ColoredFormatter(
            LOGGER_FORMAT, LOGGER_DATE_FORMAT, colorize=False
        )
        file_handler.setFormatter(file_formatter)
        self.custom_logger.addHandler(file_handler)

    def debug(self, message: str, *args, **kwargs):
        self.custom_logger.debug(message, *args, **kwargs)

    def info(self, message: str, *args, **kwargs):
        self.custom_logger.info(message, *args, **kwargs)

    def warning(self, message: str, *args, **kwargs):
        self.custom_logger.warning(message, *args, **kwargs)

    def error(self, message: str, *args, **kwargs):
        self.custom_logger.error(message, *args, **kwargs)

    def critical(self, message: str, *args, **kwargs):
        self.custom_logger.critical(message, *args, **kwargs)

    def exception(self, message: str, *args, **kwargs):
        self.custom_logger.exception(message, *args, **kwargs)