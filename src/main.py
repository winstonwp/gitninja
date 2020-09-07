import logging

logger = logging.getLogger()
logger.setLevel(logging.WARNING)
logging.basicConfig()


if __name__ == "__main__":
    logger.info("Hello World, I'm modified")
