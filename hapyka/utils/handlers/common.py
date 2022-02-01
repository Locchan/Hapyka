from hapyka.dictionaries.internal import HANDLERS_TEXT_LABEL, HANDLERS_IMAGES_LABEL, HANDLERS_COMMANDS_LABEL, \
    HANDLERS_INLINE_LABEL
from hapyka.utils.handlers import handlers


def handle_command_update(update, context):
    for ahandler in handlers[HANDLERS_COMMANDS_LABEL]:
        ahandler.handle(update, context)


def handle_text_update(update, context):
    for ahandler in handlers[HANDLERS_TEXT_LABEL]:
        ahandler.handle(update, context)


def handle_image_update(update, context):
    for ahandler in handlers[HANDLERS_IMAGES_LABEL]:
        ahandler.handle(update, context)


def handle_inline_update(update, context):
    for ahandler in handlers[HANDLERS_INLINE_LABEL]:
        ahandler.handle(update, context)
