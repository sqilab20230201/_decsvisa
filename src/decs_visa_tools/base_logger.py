"""
Logging module
"""
 
import logging
import platform
 
# Set up logs
logger = logging.getLogger(__name__)
 
# Log everything / something
#logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
 
running_on = platform.platform()
if running_on.startswith("Windows"):
    fh = logging.FileHandler('decs_visa.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
else:
    # For now, log to console (to allow PIPEd output)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
