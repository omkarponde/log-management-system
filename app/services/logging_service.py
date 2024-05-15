import logging.config
import configparser
import os


def setup_logging(config_path='app/logging_config.ini'):
    if os.path.exists(config_path):
        logging.config.fileConfig(config_path)
    else:
        raise FileNotFoundError(f"Logging configuration file not found: {config_path}")


def get_logger(logger_name):
    return logging.getLogger(logger_name)
