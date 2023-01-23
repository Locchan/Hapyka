import json
import os
from hapyka.utils.logger import get_logger
logger = get_logger()


class ConfigJson:
    def __init__(self):
        global logger
        self.config_filepath = os.environ.get('CONFIG_PATH') or "config.json"
        logger.info("Config path is {}".format(self.config_filepath))
        self.config = self.get_config()

    def get_config(self):
        if os.path.exists(self.config_filepath):
            with open(self.config_filepath, "r") as config_file:
                return json.load(config_file)
        else:
            logger.warning("File {} does not exist.".format(self.config_filepath))

    def get(self, path):
        if path in self.config:
            return self.config[path]
        else:
            return None
