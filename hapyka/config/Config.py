from hapyka.config.ConfigEnv import ConfigEnv
from hapyka.config.ConfigJson import ConfigJson
from hapyka.config.ConfigVault import ConfigVault
from hapyka.utils.logger import get_logger
logger = get_logger()
config_providers = [ConfigEnv, ConfigVault, ConfigJson]


def decide_config_provider():
    provider = None
    logger.info("Choosing config provider...")
    for aprovider in config_providers:
        logger.info("Checking provider...")
        try:
            provider = aprovider()
            if provider.config is None:
                raise
            else:
                logger.info("Provider {} seems fine. Proceeding...".format(provider.__class__.__name__))
                return provider
        except:
            logger.warning("Provider could not initialize.")
            continue
    logger.error("No valid config providers. Cannot proceed.")
    exit(1)
