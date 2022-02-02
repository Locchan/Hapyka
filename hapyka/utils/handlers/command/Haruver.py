from hapyka.dictionaries.generic import HARUKA_VER_TEMPLATE
from hapyka.utils.handlers.HaruHandler import HaruHandler
from hapyka.utils.tg_utils import reply_text
from __main__ import version, release
enabled = True
commands = ["ver", "version", "nkvdver"]


class Haruver(HaruHandler):
    def __init__(self):
        self.enabled = enabled
        super().__init__()

    def handle(self, update, context):
        for command in commands:
            if "/{command}".format(command=command) in update.message.text:
                reply_text(update, context, HARUKA_VER_TEMPLATE.format(version, release))
                return

    def enable(self):
        return self.enabled
