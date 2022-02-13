import os

from hvac import Client
from hvac.api.auth_methods.approle import AppRole
from hvac.adapters import JSONAdapter
from hapyka.utils.logger import get_logger

logger = get_logger()
import __main__

CONFIG_PATH = "kv/data/services/telegram_bots/hapyka/config"


class Config:
    def __init__(self):
        logger.info("Getting secrets...")
        self.config = {}
        self.secret_id = os.environ.get('SECRET_ID') or ""
        self.role_id = os.environ.get('ROLE_ID') or ""
        self.vault_addr = os.environ.get('VAULT_ADDR') or ""
        self.vault_port = os.environ.get('VAULT_PORT') or ""
        self.login()
        logger.info("Done getting secrets.")

    def login(self):
        try:
            if not self.secret_id or not self.role_id or not self.vault_port or not self.vault_port:
                raise RuntimeError("Cannot log in to vault: Insufficient config data.")
            url = "https://{}:{}".format(self.vault_addr, self.vault_port)
            adapter = JSONAdapter(base_uri=url)
            approle = AppRole(adapter=adapter)
            resp = approle.login(self.role_id, secret_id=self.secret_id)
            client = Client(url=url)
            if resp and resp['auth'] and resp['auth']['client_token']:
                client.token = resp['auth']['client_token']
                self.config = client.read(CONFIG_PATH)
                if self.config and self.config is not None and "data" in self.config:
                    self.config = self.config["data"]["data"]
                    return True
                else:
                    logger.error("Authenticated, but there is no config under {}".format(CONFIG_PATH))
                    exit(1)
            else:
                logger.error("Could not authenticate in vault using the provided credentials.")
                exit(1)
        except Exception as e:
            logger.error("Could not login to vault: {}".format(e.__class__.__name__))
            exit(1)

    def get(self, path):
        if path in self.config:
            return self.config[path]
        else:
            return None
