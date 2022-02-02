#!/usr/bin/env python

config_container = None
version = "0.0.1b"
release = "Press F to pay respects to NKVD-bot (R.I.P 2017-2022)"

import hapyka.utils.config
import logging
import sys

from hapyka.classes.Haruka import Haruka

from hapyka.utils.logger import get_logger

logger = get_logger()

handler = logging.StreamHandler(sys.stdout)

bot_token = config_container.get("bot_tg_token")
bot = Haruka(bot_token)
bot.start_bot()
logger.info("Haruka v{} started successfully. Release: {}".format(version, release))
