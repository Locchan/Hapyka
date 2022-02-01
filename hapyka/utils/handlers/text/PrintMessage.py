from hapyka.dictionaries.generic import START_MESSAGE
from hapyka.utils.handlers.HaruHandler import HaruHandler
from hapyka.utils.logger import get_logger
from hapyka.utils.tg_utils import reply_text, get_sender_by_update

enabled = True
msg_format = "{chat_id} in {user}: {message}"

logger = get_logger()


class PrintMessage(HaruHandler):
    def __init__(self):
        self.enabled = enabled
        super().__init__()

    def handle(self, update, context):
        if update.message:
            if update.message.text:
                logger.info("Message: {}: {}".format(get_sender_by_update(update), update.message.text))

    def enable(self):
        return self.enabled
