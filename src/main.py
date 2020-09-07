import logging

logger = logging.getLogger()
logger.setLevel(logging.ERROR)
logging.basicConfig()


if __name__ == "__main__":
    logger.info("Hello World!")
