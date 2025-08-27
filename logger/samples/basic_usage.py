from logger import log


def main():
    log.info("Starting application")
    log.debug("Debug message")
    log.warning("Warning message")
    log.error("Error message")
    log.critical("Critical message")

    try:
        _ = 10 / 0
    except ZeroDivisionError:
        log.exception("Division by zero error")


if __name__ == "__main__":
    main()
