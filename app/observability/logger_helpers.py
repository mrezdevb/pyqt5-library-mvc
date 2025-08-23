from app.observability.log_context import get_trace_id, get_user_id, get_extra_data
from logging import Logger
from typing import Any


def log_json(logger: Logger, level: str, action: str, msg: str='', **extra: Any) -> None:
    data: dict[str, Any] = {
        "action": action,
        "msg": msg,
        "trace_id": get_trace_id(),
        "user_id": get_user_id(),
        **get_extra_data(),
        **extra,
    }


    getattr(logger, level)("", extra={"extra_data": data})
