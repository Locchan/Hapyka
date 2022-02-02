from hapyka.dictionaries.generic import START_MESSAGE
from hapyka.utils.handlers.HaruHandler import HaruHandler
from hapyka.utils.tg_utils import reply_text

enabled = True
command = "start"


class Start(HaruHandler):
    def __init__(self):
        self.enabled = enabled
        super().__init__()

    def handle(self, update, context):
        if "/{command}".format(command=command) in update.message.text:
            reply_text(update, context, START_MESSAGE)

    def enable(self):
        return self.enabled
