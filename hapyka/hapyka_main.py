#!/usr/bin/env python3
from hapyka.config.Config import decide_config_provider
from hapyka.utils.logger import get_logger, setdebug
import datetime

version = "1.1.4.3"
release = '''
Релиз 10:
Фикс репостера
'''

logger = get_logger()
logger.info("Starting Hapyka {}...".format(version))


start_time = datetime.datetime.now()
logger.info("Getting config...")
config_provider = decide_config_provider()

if config_provider.get("debug"):
    setdebug()

import logging
import sys

from hapyka.utils.logger import get_logger
logger = get_logger()

from hapyka.database.db import initialize
initialize()

from hapyka.classes.Haruka import Haruka

handler = logging.StreamHandler(sys.stdout)
bot_token = config_provider.get("bot_tg_token")
hapyka = Haruka(bot_token)

from hapyka.utils.chrono_threading import start_chrono_threads

start_chrono_threads()
finished_loading_time = datetime.datetime.now()
load_time = "{:.2f}".format(finished_loading_time.timestamp() - start_time.timestamp())

logger.info("Haruka v{} started successfully in {}s. Release: {}".format(version, load_time, release))
