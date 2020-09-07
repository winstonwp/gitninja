import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig()


if __name__ == "__main__":
    logger.info("Hello World!")
