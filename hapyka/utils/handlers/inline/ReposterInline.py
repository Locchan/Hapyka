import re
import os

from hapyka.dictionaries.generic import REPOSTER_DISCARD_CALLBACK_DATA, REPOSTER_CAPTION_REGEX, \
    REPOSTER_CAPTION_TEMPLATE, REPOSTER_INLINE_MARKER
from hapyka.utils.handlers.HaruHandler import HaruHandler
from __main__ import config_provider
from hapyka.utils.logger import get_logger

enabled = True
logger = get_logger()


class ReposterInline(HaruHandler):
    def __init__(self):
        self.enabled = enabled
        self.reposter_anon = config_provider.get("reposter/anon")
        self.reposter_dir = config_provider.get("reposter/directory")
        if not os.path.exists(self.reposter_dir):
            logger.info("{} does not exist. Creating...".format(self.reposter_dir))
            os.makedirs(self.reposter_dir)
        super().__init__()

    def handle_impl(self, update, context):
        callback_data = update.callback_query.data
        if not callback_data.startswith(REPOSTER_INLINE_MARKER):
            return
        logger.info("Reposter: Processing inline update.")
        try:
            callback_data = int(callback_data.replace(REPOSTER_INLINE_MARKER, ''))
        except ValueError:
            callback_data = callback_data.replace(REPOSTER_INLINE_MARKER, '')
        if callback_data == REPOSTER_DISCARD_CALLBACK_DATA:
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.callback_query.message.message_id)
            logger.info("Reposter: Discarding.")
        else:
            file_id = update.callback_query.message.photo[-1].file_id
            with open("{}/{}.png".format(self.reposter_dir, file_id), 'wb') as img_file:
                context.bot.get_file(file_id=file_id).download(out=img_file)
            if callback_data not in self.reposter_anon:
                with open("{}/{}.txt".format(self.reposter_dir, file_id), "w") as caption_file:
                    caption_file.write("{}\n{}".format(callback_data, update.callback_query.message.caption))
                logger.info("Reposter: File saved.")
            else:
                caption_fragments = list(re.search(REPOSTER_CAPTION_REGEX, update.callback_query.message.caption).groups())
                caption_post = REPOSTER_CAPTION_TEMPLATE.format("??????????", caption_fragments[1])
                with open("{}/{}.txt".format(self.reposter_dir, file_id), "w") as caption_file:
                    caption_file.write("{}\n{}".format(callback_data, caption_post))
                logger.info("Reposter: Anonymous file saved")
            context.bot.delete_message(chat_id=update.effective_chat.id,
                                       message_id=update.callback_query.message.message_id)

    def enable(self):
        return self.enabled
