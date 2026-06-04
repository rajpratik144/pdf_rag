import logging
import os


LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(name: str):

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        os.path.join(LOG_DIR, "application.log")
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger