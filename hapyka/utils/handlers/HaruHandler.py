from hapyka.utils.logger import get_logger

logger = get_logger()


class HaruHandler:
    def __init__(self):
        self.disable_reason = ""
        try:
            self.enabled = self.enable()
        except Exception as e:
            self.enabled = False
            self.disable_reason = "Error: {}".format(e.__class__.__name__)
        if self.enabled is None:
            self.enabled = False
            self.disable_reason = "Could not enable. Got None as enabling result."
        if isinstance(self.enabled, tuple):
            self.disable_reason = self.enabled[1]
            self.enabled = self.enabled[0]
        if self.enabled:
            logger.debug("{} handler enabled".format(self.__class__.__name__, self.enabled))
        else:
            if self.disable_reason:
                logger.info(
                    "{} handler is disabled. Reason: {}".format(self.__class__.__name__, self.disable_reason))
            else:
                logger.info("{} handler is disabled.".format(self.__class__.__name__))

    def enable(self):
        pass

    def __handle__(self, update, context):
        return self.handle_impl(update, context)

    def handle_impl(self, update, context):
        pass
