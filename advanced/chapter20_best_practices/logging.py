# logging.py
# Examples and explanations for logging

import logging

# Basic configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Logging messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Creating a custom logger
logger = logging.getLogger('exampleLogger')
logger.setLevel(logging.DEBUG)

# Create handler and set level to debug
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add handler to logger
logger.addHandler(handler)

logger.debug('Debug message from custom logger')
logger.info('Info message from custom logger')
logger.warning('Warning message from custom logger')
logger.error('Error message from custom logger')
logger.critical('Critical message from custom logger')
