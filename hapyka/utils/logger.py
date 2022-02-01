import logging
import sys

_log_format = "%(asctime)s - [%(levelname)s] - Hapyka: %(name)s.py - %(message)s"

loggers = {

}


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    stream_handler.setStream(sys.stdout)
    return stream_handler


def get_logger(name="Hapyka"):
    if name in loggers:
        return loggers[name]
    else:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        logger.addHandler(get_stream_handler())
        loggers[name] = logger
        return loggers[name]
