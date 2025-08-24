import uuid
from functools import wraps
from typing import Any, Callable, TypeVar, cast

from app.observability.log_context import set_trace_id
from app.observability.logger import get_logger

log = get_logger("Tracer")


F = TypeVar("F", bound=Callable[..., Any])


def traced(action_name: str) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            trace_id = uuid.uuid4().hex[:8]
            set_trace_id(trace_id)
            log.info(f"[TRACE] {action_name} started")

            try:
                result = func(*args, **kwargs)
                log.info(f"[TRACE] {action_name} completed")
                return result

            except Exception as e:
                log.exception(f"[TRACE] {action_name} failed: {e}")
                raise

        return cast(F, wrapper)

    return decorator
