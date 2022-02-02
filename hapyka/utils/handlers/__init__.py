from telegram.ext import CommandHandler

from hapyka.dictionaries.internal import HANDLERS_IMAGES_LABEL, HANDLERS_COMMANDS_LABEL, HANDLERS_TEXT_LABEL, \
    HANDLERS_INLINE_LABEL
from hapyka.utils.handlers.command import command_handlers
from hapyka.utils.handlers.image import image_handlers
from hapyka.utils.handlers.inline import inline_handlers
from hapyka.utils.handlers.text import text_handlers
from hapyka.utils.logger import get_logger

logger = get_logger()

logger.info("Initializing handlers...")

created_objs = []


def check_obj_exists(aclass):
    for anobj in created_objs:
        if isinstance(anobj, aclass):
            return anobj
    return False


handlers_classes = {
    HANDLERS_COMMANDS_LABEL: command_handlers,
    HANDLERS_TEXT_LABEL: text_handlers,
    HANDLERS_IMAGES_LABEL: image_handlers,
    HANDLERS_INLINE_LABEL: inline_handlers
}


handlers = {

}

for handler_type, handlers_list in handlers_classes.items():
    for ahandler in handlers_list:
        if handler_type not in handlers:
            handlers[handler_type] = []
        handler = check_obj_exists(ahandler)
        if not handler:
            handler = ahandler()
            if handler.enabled:
                created_objs.append(handler)
                handlers[handler_type].append(handler)
        else:
            handlers[handler_type].append(handler)

enabled_handlers = ", ".join([x.__class__.__name__ for x in created_objs])

logger.info("Done initializing handlers.")
logger.info("Enabled handlers: {}".format(enabled_handlers))