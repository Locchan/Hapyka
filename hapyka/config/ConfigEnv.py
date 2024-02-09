import json
import os
from hapyka.utils.logger import get_logger
logger = get_logger()


class ConfigEnv:
    def __init__(self):
        global logger
        self.enabled = os.environ.get('CONFIG_ENV') == "1"
        logger.info("CONFIG_ENV is set. Getting config from environment")
        self.config = self.get_config()

    def get_config(self):
        return os.environ

    def get(self, path):
        if path in self.config:
            return self.config[path]
        else:
            return None
