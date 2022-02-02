from hapyka.dictionaries.generic import START_MESSAGE
from hapyka.utils.handlers.command.CommandHanlder import CommandHandler
from hapyka.utils.tg_utils import reply_text

enabled = True


class Start(CommandHandler):
    def __init__(self):
        self.enabled = enabled
        self.commands = ["start", "meh"]
        super().__init__()

    def handle_impl(self, update, context):
        reply_text(update, context, START_MESSAGE)

    def enable(self):
        return self.enabled
