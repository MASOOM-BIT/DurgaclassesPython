#To create a log file and write warning and higher level message

import logging

logging.basicConfig(filename='log.txt',level=logging.WARNING)
print("Logging demo ..")

logging.debug("Dubug Message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error Message")
logging.critical("Critical message")

