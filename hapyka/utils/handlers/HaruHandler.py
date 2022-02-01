from hapyka.utils.logger import get_logger
logger = get_logger()


class HaruHandler:
    def __init__(self):
        self.enabled = self.enable()
        self.disable_reason = ""
        if self.enabled is not None:
            if isinstance(self.enabled, tuple):
                self.disable_reason = self.enabled[1]
                self.enabled = self.enabled[0]
            if self.enabled:
                logger.info("{} handler enabled".format(self.__class__.__name__, self.enabled))
            else:
                if self.disable_reason:
                    logger.info("{} handler is disabled. Reason: {}".format(self.__class__.__name__, self.disable_reason))
                else:
                    logger.info("{} handler is disabled.".format(self.__class__.__name__))

        pass

    def enable(self):
        pass

    def handle(self, update, context):
        pass