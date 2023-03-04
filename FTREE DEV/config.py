from loguru import logger

FILE_PATH = ""
LEVEL = 0
PREFIX = LEVEL*"└───"

# LOGURU SETTINGS

DEBUG = False
DEBUG_LEVEL = "DEBUG" 

"""
TRACE 	  |  5 	|    logger.trace()
DEBUG 	  | 10 	|    logger.debug()
INFO 	  | 20 	|    logger.info()
SUCCESS   | 25 	|    logger.success()
WARNING   | 30 	|    logger.warning()
ERROR 	  | 40 	|    logger.error()
CRITICAL  | 50 	|    logger.critical()
"""

logger.add("debug.log", format = "{time} {level} {message}", level = "DEBUG", rotation="10 MB", compression="zip", diagnose = DEBUG)

