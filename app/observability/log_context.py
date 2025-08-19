from contextvars import ContextVar


trace_id_var = ContextVar('trace_id', default=None)
user_id_var = ContextVar('user_id', default=None)
extra_data_var = ContextVar('extra_data', default={})


def set_trace_id(trace_id: str):
	trace_id_var.set(trace_id)



def get_trace_id() -> str:
	return trace_id_var.get()



def set_user_id(user_id):
	user_id_var.set(user_id)



def get_user_id():
	return user_id_var.get()



def set_extra_data(data: dict):
	current = extra_data_var.get() or {}
	current.update(data)
	extra_data_var.set(current)



def get_extra_data() -> dict:
	return extra_data_var.get() or {}



def clear_context():
	trace_id_var.set(None)
	user_id_var.set(None)
	extra_data_var.set({})



