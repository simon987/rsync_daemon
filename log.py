import logging
import sys
from logging import StreamHandler

DATE_FMT = "%Y-%m-%d %H:%M:%S"

stdout_logger = logging.getLogger("default")
stdout_logger.setLevel(logging.DEBUG)

for h in stdout_logger.handlers:
    stdout_logger.removeHandler(h)

handler = StreamHandler(sys.stdout)
fmt = "%(asctime)s %(levelname)-5s>%(message)s"
handler.formatter = logging.Formatter(fmt, datefmt='%Y-%m-%d %H:%M:%S')

stdout_logger.addHandler(handler)
logger = stdout_logger
