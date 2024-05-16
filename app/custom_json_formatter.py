import logging
import json
import time


class CustomJsonFormatter(logging.Formatter):
    def __init__(self, source_path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.source_path = source_path

    def format(self, record):
        # Create log entry
        log_entry = {
            "level": record.levelname.lower(),
            "log_string": record.getMessage(),
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(record.created)),
            "metadata": {
                "source": self.source_path
            }
        }
        return json.dumps(log_entry)

    def formatException(self, ei):
        exception_data = super().formatException(ei)
        return json.dumps({"exception": exception_data})

    def formatStack(self, stack_info):
        stack_data = super().formatStack(stack_info)
        return json.dumps({"stack": stack_data})
