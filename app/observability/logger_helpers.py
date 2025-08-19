from app.observability.log_context import get_trace_id, get_user_id, get_extra_data




def log_json(logger, level, action, msg='', **extra):
    data = {
        "action": action,
        "msg": msg,
        "trace_id": get_trace_id(),
        "user_id": get_user_id(),
        **get_extra_data(),
        **extra,
    }


    getattr(logger, level)("", extra={"extra_data": data})
