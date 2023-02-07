from hapyka.dictionaries.generic import WHO_TEMPLATE
from hapyka.handlers.HaruHandler import HaruHandler
from hapyka.handlers.command.CommandHanlder import CommandHandler
from hapyka.utils.tg_utils import reply_text, get_chat_by_update, get_sender_by_update, get_sender_by_message

enabled = True


class Who(CommandHandler):
    def __init__(self):
        self.enabled = enabled
        self.commands = ["who", "whois", "nkvdinfo"]
        super().__init__()

    def handle_impl(self, update, context):
        if update.message.reply_to_message:
            reply_text(update, context,
                       WHO_TEMPLATE.format(get_sender_by_message(update.message.reply_to_message),
                                           get_chat_by_update(update)))
        else:
            reply_text(update, context,
                       WHO_TEMPLATE.format(get_sender_by_update(update), get_chat_by_update(update)))

    def enable(self):
        return self.enabled
