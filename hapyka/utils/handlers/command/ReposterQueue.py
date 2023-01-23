from hapyka.dictionaries.generic import REPOSTER_QUEUE_TEMPLATE
from hapyka.utils.handlers.command.CommandHanlder import CommandHandler
from hapyka.utils.reposter import get_pics_to_repost
from hapyka.utils.tg_utils import reply_text

enabled = True


class ReposterQueue(CommandHandler):
    def __init__(self):
        self.enabled = enabled
        self.commands = ["reposter_queue", "queue"]
        super().__init__()

    def handle_impl(self, update, context):
        reply_text(update, context,
                   REPOSTER_QUEUE_TEMPLATE.format(len(get_pics_to_repost())))

    def enable(self):
        return self.enabled
