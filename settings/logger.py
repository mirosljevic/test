from utils.config import get_config_var


LOGGER_ENABLE_ALLURE = get_config_var("LOGGER_ENABLE_ALLURE", False)
LOGGER_LOG_LEVEL = get_config_var("LOGGER_LOG_LEVEL", "DEBUG")
LOGGER_LOG_TO_FILE = get_config_var("LOGGER_LOG_TO_FILE", False)
LOGGER_LOG_FILE_PATH = get_config_var("LOGGER_LOG_FILE_PATH", "log/execution.log")
LOGGER_COLORIZE_OUTPUT = get_config_var("LOGGER_COLORIZE_OUTPUT", True)
LOGGER_DATE_FORMAT = get_config_var("LOGGER_DATE_FORMAT", "%Y-%m-%d %H:%M:%S")
LOGGER_FORMAT = get_config_var(
    "LOGGER_FORMAT", "%(asctime)s - %(levelname)s - %(message)s"
)
