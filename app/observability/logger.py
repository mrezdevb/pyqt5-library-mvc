import os
import sys
import logging
import json
from datetime import datetime
from .log_context import get_trace_id, get_user_id, get_extra_data
from typing import Any

BASE_DIR: str = os.path.abspath(os.getcwd())  
LOG_DIR: str = os.path.join(BASE_DIR, "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE: str = os.path.join(LOG_DIR, "library.log")





class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_data: dict[str, Any] = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "trace_id": get_trace_id(),
            "user_id": get_user_id(),
            **get_extra_data(),
        }
        if hasattr(record, "extra_data"):
            log_data.update(record.extra_data)
        else:
            log_data["msg"] = record.getMessage()
        return json.dumps(log_data, ensure_ascii=False, indent=2)


def get_logger(name: str) -> logging.Logger:
    logger: logging.Logger = logging.getLogger(name)
    if not logger.handlers:
      
        consule_handler: logging.StreamHandler = logging.StreamHandler(sys.stdout)
        consule_handler.setFormatter(JsonFormatter())
        logger.addHandler(consule_handler)

     
        file_handler: logging.FileHandler = logging.FileHandler(LOG_FILE, encoding="utf-8")
        file_handler.setFormatter(JsonFormatter())
        logger.addHandler(file_handler)

        logger.setLevel(logging.DEBUG)
  
    return logger
