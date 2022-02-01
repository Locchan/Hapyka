from telegram.ext import CommandHandler

from hapyka.dictionaries.internal import HANDLERS_IMAGES_LABEL, HANDLERS_COMMANDS_LABEL, HANDLERS_TEXT_LABEL, \
    HANDLERS_INLINE_LABEL
from hapyka.utils.handlers.command import command_handlers
from hapyka.utils.handlers.image import image_handlers
from hapyka.utils.handlers.inline import inline_handlers
from hapyka.utils.handlers.text import text_handlers

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
        handlers[handler_type].append(ahandler())
