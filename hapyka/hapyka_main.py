#!/usr/bin/env python
from hapyka.config.Config import decide_config_provider

print("Starting Hapyka...")

import datetime

start_time = datetime.datetime.now()
print("Getting config...")
config_provider = decide_config_provider()

version = "1.1.0 (release 5)"
release = '''
Reposter update.
'''

import logging
import sys

from hapyka.utils.logger import get_logger
logger = get_logger()

from hapyka.database.db import initialize
initialize()

from hapyka.classes.Haruka import Haruka

handler = logging.StreamHandler(sys.stdout)

bot_token = config_provider.get("bot_tg_token")
bot = Haruka(bot_token)

finished_loading_time = datetime.datetime.now()
load_time = "{:.2f}".format(finished_loading_time.timestamp() - start_time.timestamp())

logger.info("Haruka v{} started successfully in {}s. Release: {}".format(version, load_time, release))
