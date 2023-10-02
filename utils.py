import logging
from typing_extensions import Literal
from rich.logging import RichHandler
import time


def get_logger(name: str, level: Literal["info", "warning", "debug"]) -> logging.Logger:
    rich_handler = RichHandler(level=logging.INFO, rich_tracebacks=True, markup=True)

    logger = logging.getLogger(name)
    logger.setLevel(logging._nameToLevel[level.upper()])

    if not logger.handlers:
        logger.addHandler(rich_handler)

    logger.propagate = False

    return logger

timers={}

def start_timer(timer_name):
    global timers
    timers[timer_name] = time.time()

def elapsed_time(timer_name, text):
    global timers
    current = time.time()
    delta = current - timers[timer_name]
    timers[timer_name] = current
    if text:
        print(timer_name+" "+text+" duration "+str(delta))
    