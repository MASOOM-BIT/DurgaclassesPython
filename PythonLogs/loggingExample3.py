import logging
#To include timestamp in logging file

logging.basicConfig(
    filename='log1.txt',
    level=logging.WARNING,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

print("Logging demo ..")

logging.debug("Debug Message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error Message")
logging.critical("Critical message")