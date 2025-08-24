from contextvars import ContextVar
from typing import Optional

trace_id_var: ContextVar[Optional[str]] = ContextVar("trace_id", default=None)
user_id_var: ContextVar[Optional[str]] = ContextVar("user_id", default=None)
extra_data_var: ContextVar[dict] = ContextVar("extra_data", default={})


def set_trace_id(trace_id: str) -> None:
    trace_id_var.set(trace_id)


def get_trace_id() -> Optional[str]:
    return trace_id_var.get()


def set_user_id(user_id: str) -> None:
    user_id_var.set(user_id)


def get_user_id() -> Optional[str]:
    return user_id_var.get()


def set_extra_data(data: dict) -> None:
    current = extra_data_var.get() or {}
    current.update(data)
    extra_data_var.set(current)


def get_extra_data() -> dict:
    return extra_data_var.get() or {}


def clear_context() -> None:
    trace_id_var.set(None)
    user_id_var.set(None)
    extra_data_var.set({})
