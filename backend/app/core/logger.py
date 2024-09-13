import logging
from logging import getLogger, basicConfig, INFO

logger = getLogger(__name__)

def setup_logger():
    """
    Sets up the logger with a predefined format and log level.
    """
    # Configure the logging format and log level
    basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=INFO
    )

    # Set the log level to INFO by default
    logger.setLevel(INFO)