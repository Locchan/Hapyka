from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler

from hapyka.utils.handlers.CommonHandler import CommonHandler
from hapyka.utils.logger import get_logger

logger = get_logger()


class Haruka:
    def __init__(self, token):
        logger.info("Starting bot...")
        self.token = token
        self.common_handler = CommonHandler()
        self.upd_obj = Updater(token=self.token, use_context=True)
        self.start_bot()
        logger.info("Done starting bot.")

    def start_bot(self):
        dispatcher = self.upd_obj.dispatcher
        dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), self.common_handler.handle_text_update))
        dispatcher.add_handler(MessageHandler(Filters.command, self.common_handler.handle_command_update))
        dispatcher.add_handler(MessageHandler(Filters.photo, self.common_handler.handle_image_update))
        dispatcher.add_handler(CallbackQueryHandler(self.common_handler.handle_inline_update, pass_user_data=True, ))
        dispatcher.add_error_handler(self.handle_exception)
        self.upd_obj.start_polling()

    def handle_exception(self, update, context):
        try:
            raise context.error
        except Exception as e:
            logger.exception(e)
