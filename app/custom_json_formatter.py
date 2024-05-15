import logging
import json
import time


class CustomJsonFormatter(logging.Formatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def format(self, record):
        log_file_path = self._get_log_file_path(record)
        log_entry = {
            "level": record.levelname.lower(),
            "log_string": record.getMessage(),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(record.created)),
            "metadata": {
                "source": log_file_path
            }
        }
        return json.dumps(log_entry)

    def _get_log_file_path(self, record):
        logger_name = record.name
        if logger_name.startswith('auth'):
            return "./logs/auth/app.log"
        elif logger_name.startswith('order'):
            return "./logs/order/app.log"
        elif logger_name.startswith('product'):
            return "./logs/product/app.log"
        else:
            return "unknown"
