from hapyka.dictionaries.generic import REPOSTER_DISCARD_CALLBACK_DATA
from hapyka.utils.handlers.HaruHandler import HaruHandler

enabled = True


class ReposterInline(HaruHandler):
    def __init__(self):
        self.enabled = enabled
        super().__init__()

    def handle_impl(self, update, context):
        callback_data = update.callback_query.data
        if callback_data == REPOSTER_DISCARD_CALLBACK_DATA:
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.callback_query.message.message_id)
        else:
            context.bot.send_photo(callback_data, photo=update.callback_query.message.photo[-1], caption=update.callback_query.message.caption)
            context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.callback_query.message.message_id)

    def enable(self):
        return self.enabled