import threading
import time

from hapyka.utils.logger import get_logger
from hapyka.utils.reposter import reposter_repost_picture

chrono_minutely_fn = [reposter_repost_picture]
chrono_threads = []
logger = get_logger()


def start_chrono_threads():
    logger.info("Starting chrono threads...")
    minutely_thread = threading.Thread(name="CHRThreadM", target=chrono_minutely)
    minutely_thread.start()
    chrono_threads.append(minutely_thread)
    logger.info("Done starting threads.")
    pass


def chrono_minutely():
    logger.info("Minutely thread started.")
    while True:
        logger.debug("Minutely thread tick.")
        for afunc in chrono_minutely_fn:
            logger.debug("Executing {}".format(afunc.__name__))
            try:
                afunc()
            except Exception as e:
                logger.error("Failed to run {}: {}".format(afunc.__name__, e.__class__.__name__))
                logger.exception(e)
        time.sleep(60)
        pass
