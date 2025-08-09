import logging

logging.basicConfig(
	level = logging.INFO, 
	format="[%(levelname)s] %(asctime)s - %(name)s - %(message)s",
	handlers=[
		logging.FileHandler("library.log"),
		logging.StreamHandler()
		]
		)
def get_logger(name):
	return logging.getLogger(name)
