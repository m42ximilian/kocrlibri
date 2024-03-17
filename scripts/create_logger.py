import logging
from logging.handlers import RotatingFileHandler

def logger(name, log_file, level=logging.INFO):
    """
    Creates and configures a logger.

    :param name: Logger name.
    :param log_file: File path for the logger to write logs.
    :param level: Logging level.
    :return: Configured logger.
    """
    # Create a logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create a file handler for the logger
    handler = RotatingFileHandler(log_file, maxBytes=10000000, backupCount=5)
    handler.setLevel(level)

    # Create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    
    # Avoid logging propagation to the root logger
    logger.propagate = False

    return logger
