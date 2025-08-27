from logger import log


def main():
    log.info("This message will be logged to file")
    log.error("Error message to file")
    log.warning("Warning message to file")


if __name__ == "__main__":
    main()

# To run this script, ensure you have the logger configured to log to a file.
# LOGGER_LOG_TO_FILE=true LOGGER_LOG_FILE_PATH=log/sample.log python logger/samples/custom_logger.py
