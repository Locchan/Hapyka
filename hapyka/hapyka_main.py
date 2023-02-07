#!/usr/bin/env python3
from hapyka.config.Config import decide_config_provider
from hapyka.utils.logger import get_logger
import datetime

version = "1.1.2.1"
release = '''
Релиз 6: Апдейт репостера.
- Теперь репостит рандомную картинку из списка, а не первую по алфавиту.
- Скорость постинга репостера теперь меняется в зависимости от размера очереди.
- Команда /queue (/reposter_queue) заменена на команду /reposter и теперь выводит всю информацию о состоянии репостера.
'''

logger = get_logger()
logger.info("Starting Hapyka {}...".format(version))


start_time = datetime.datetime.now()
logger.info("Getting config...")
config_provider = decide_config_provider()

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
