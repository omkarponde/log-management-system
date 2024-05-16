import logging.config
import configparser
from app.custom_json_formatter import CustomJsonFormatter

# Read logging configuration from INI file
config = configparser.ConfigParser()
config.read('./app/logging_config.ini')


# for logger_name in ["auth_logger", "order_logger", "product_logger"]:
def get_logger(logger_name):
    logging.config.fileConfig('./app/logging_config.ini')
    logger = logging.getLogger(logger_name)
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            handler.setFormatter(CustomJsonFormatter())
    return logger
