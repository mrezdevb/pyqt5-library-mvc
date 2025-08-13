from library_app.utils.logger import get_logger
import logging



def test_get_logger_returns_logger_instance():
	logger = get_logger('TestLogger')
	assert isinstance(logger, logging.Logger)
	assert logger.name == 'TestLogger'
	assert logger.level == logging.INFO or logger.level ==0
def test_logger_can_log(caplog):
	logger = get_logger('TestLogger')
	with caplog.at_level(logging.INFO):
		logger.info('This is a test log.')
	assert 'This is a test log.' in caplog.text
