"""
Logging module
"""

import logging

# Set up logs
logger = logging.getLogger(__name__)

# Log everything / something
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

# For now, log to console
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
