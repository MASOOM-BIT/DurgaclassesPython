#it will display exception in the log file

#syntax : logging.exception(msg)

import logging
logging.basicConfig(
    filename='Explogfile.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logging.info("A new Request")
try:
    x=int(input("1st No :"))
    y=int(input("2nd No"))
    print(x/y)
except ZeroDivisionError as msg1:
    print(msg1)
    logging.exception(msg1)
except ValueError as msg2:
    print(msg2)
    logging.exception(msg2)

logging.info("Request Completed")