import logging.config
import configparser
from app.custom_json_formatter import CustomJsonFormatter

# Read logging configuration from INI file
config = configparser.ConfigParser()
config.read('./app/logging_config.ini')

# Configure logging
logging.config.fileConfig('./app/logging_config.ini')


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            if 'app.log' in handler.baseFilename:
                service_name = logger_name.split('_')[0]
                source_path = f'./app/tmp/logs/{service_name}/app.log'
            elif 'error.log' in handler.baseFilename:
                service_name = logger_name.split('_')[0]
                source_path = f'./app/tmp/logs/{service_name}/error.log'
            handler.setFormatter(CustomJsonFormatter(source_path))
    return logger
