from hapyka.dictionaries.generic import INLINE_PRINT_TEMPLATE
from hapyka.handlers.HaruHandler import HaruHandler
from hapyka.utils.logger import get_logger
from hapyka.utils.tg_utils import get_chat_by_update

enabled = True

logger = get_logger()


class PrintInline(HaruHandler):
    def __init__(self):
        self.enabled = enabled
        super().__init__()

    def handle_impl(self, update, context):
        callback_data = update.callback_query.data
        logger.info(INLINE_PRINT_TEMPLATE.format(get_chat_by_update(update, with_id=False), callback_data))

    def enable(self):
        return self.enabled