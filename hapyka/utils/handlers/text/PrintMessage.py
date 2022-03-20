from hapyka.dictionaries.generic import MESSAGE_PRINT_TEMPLATE
from hapyka.utils.handlers.HaruHandler import HaruHandler
from hapyka.utils.logger import get_logger
from hapyka.utils.tg_utils import get_sender_by_update, get_chat_by_update

enabled = True
msg_format = "{chat_id} in {user}: {message}"

logger = get_logger()


class PrintMessage(HaruHandler):
    def __init__(self):
        self.enabled = enabled
        super().__init__()

    def handle_impl(self, update, context):
        if update.message:
            if update.message.text:
                logger.info(MESSAGE_PRINT_TEMPLATE.format(get_chat_by_update(update, with_id=False),
                                                          get_sender_by_update(update, with_id=False),
                                                          update.message.text.replace("\n", " ")))

    def enable(self):
        return self.enabled
