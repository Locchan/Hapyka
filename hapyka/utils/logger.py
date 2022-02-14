import logging
import sys

_log_format = "%(asctime)s - [%(levelname)s] - Hapyka: %(name)s.py - %(message)s"

loggers = {

}

level = logging.INFO


def get_stream_handler():
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_logger(name="Hapyka"):
    global level
    if name in loggers:
        if loggers[name].level == level:
            return loggers[name]
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if name not in loggers:
        logger.addHandler(get_stream_handler())
    loggers[name] = logger
    return loggers[name]


def setdebug():
    global level
    level = logging.DEBUG
