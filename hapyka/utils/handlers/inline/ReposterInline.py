import re

from hapyka.dictionaries.generic import REPOSTER_DISCARD_CALLBACK_DATA, REPOSTER_CAPTION_REGEX, \
    REPOSTER_CAPTION_TEMPLATE, REPOSTER_INLINE_MARKER
from hapyka.utils.handlers.HaruHandler import HaruHandler
from __main__ import config_container

from hapyka.utils.logger import get_logger

enabled = True

logger = get_logger()


class ReposterInline(HaruHandler):
    def __init__(self):
        self.enabled = enabled
        self.reposter_anon = config_container.get("reposter/anon")
        super().__init__()

    def handle_impl(self, update, context):
        callback_data = update.callback_query.data
        if not callback_data.startswith(REPOSTER_INLINE_MARKER):
            return
        logger.info("Reposter: Processing inline update.")
        callback_data = int(callback_data.replace(REPOSTER_INLINE_MARKER, ''))
        if callback_data == REPOSTER_DISCARD_CALLBACK_DATA:
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.callback_query.message.message_id)
            logger.info("Reposter: Discarding.")
        else:
            if callback_data not in self.reposter_anon:
                context.bot.send_photo(callback_data, photo=update.callback_query.message.photo[-1], caption=update.callback_query.message.caption)
                context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.callback_query.message.message_id)
                logger.info("Reposter: Reposting.")
            else:
                caption_fragments = list(re.search(REPOSTER_CAPTION_REGEX, update.callback_query.message.caption).groups())
                caption_post = REPOSTER_CAPTION_TEMPLATE.format("??????????", caption_fragments[1])
                context.bot.send_photo(callback_data, photo=update.callback_query.message.photo[-1], caption=caption_post)
                context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.callback_query.message.message_id)
                logger.info("Reposter: Reposting anonymously.")

    def enable(self):
        return self.enabled
