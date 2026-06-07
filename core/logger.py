# ==========================================
# File: core/logger.py
# ==========================================


import logging
import os

from config import Config

Config.LOG_DIR.mkdir(parents=True,exist_ok=True)


def get_logger(name: str):

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        Config.LOG_DIR / "application.log"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger