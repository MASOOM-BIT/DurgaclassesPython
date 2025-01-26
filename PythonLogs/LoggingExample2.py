import logging

#If i want inform and debug message

logging.basicConfig(filename='RESOURCES/log2.txt',level=logging.DEBUG)
print("Logging demo ..")

logging.debug("Dubug Message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error Message")
logging.critical("Critical message")