from logger import log
from logger.colors import LogColor


def main():
    log.info("Testing different log levels")

    log.debug("Debug level - dark grey")
    log.info("Info level - green")
    log.warning("Warning level - yellow")
    log.error("Error level - red")
    log.critical("Critical level - magenta")

    print(f"Available colors: {list(LogColor)}")


if __name__ == "__main__":
    main()
