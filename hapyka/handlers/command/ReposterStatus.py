from hapyka.dictionaries.generic import REPOSTER_STATUS_TEMPLATE
from hapyka.handlers.command.CommandHanlder import CommandHandler
from hapyka.utils.tg_utils import reply_text
from hapyka.utils.reposter import get_reposter_status

enabled = True


class ReposterStatus(CommandHandler):
    def __init__(self):
        self.enabled = enabled
        self.commands = ["reposter"]
        super().__init__()

    def handle_impl(self, update, context):
        reply_text(update, context, REPOSTER_STATUS_TEMPLATE.format(*get_reposter_status()))

    def enable(self):
        return self.enabled
