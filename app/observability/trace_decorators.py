import uuid
from functools import wraps
from app.observability.log_context import set_trace_id
from app.observability.logger import get_logger


log = get_logger('Tracer')



def traced(action_name):
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			trace_id = uuid.uuid4().hex[:8]
			set_trace_id(trace_id)
			log.info(f'[TRACE] {action_name} started')


			try:
				result = func(*args, **kwargs)
				log.info(f'[TRACE] {action_name} completed')
				return result



			except Exception as e:
				log.exception(f'[TRACE] {action_name} failed: {e}')
				raise


		return wrapper
	
	
	return decorator
