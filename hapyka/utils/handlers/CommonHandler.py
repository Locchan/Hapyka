from hapyka.dictionaries.internal import HANDLERS_TEXT_LABEL, HANDLERS_IMAGES_LABEL, HANDLERS_COMMANDS_LABEL, \
    HANDLERS_INLINE_LABEL
from hapyka.utils.handlers import handlers


class CommonHandler:
    def handle_command_update(self, update, context):
        for ahandler in handlers[HANDLERS_COMMANDS_LABEL]:
            ahandler.__handle__(update, context)


    def handle_text_update(self, update, context):
        for ahandler in handlers[HANDLERS_TEXT_LABEL]:
            ahandler.__handle__(update, context)


    def handle_image_update(self, update, context):
        for ahandler in handlers[HANDLERS_IMAGES_LABEL]:
            ahandler.__handle__(update, context)


    def handle_inline_update(self, update, context):
        for ahandler in handlers[HANDLERS_INLINE_LABEL]:
            ahandler.__handle__(update, context)
