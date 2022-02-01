def reply_text(update, context, message):
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def get_sender_by_update(update, with_id=True, with_username=True):
    message = update.message
    if message.from_user is not None:
        user_id = message.from_user.id
        username = message.from_user.username
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        res = ""
        if first_name:
            res += first_name
            if last_name:
                res += "{}".format(last_name)
        if with_username and username:
            if with_id:
                res += " @{username}({user_id})".format(username=username, user_id=user_id)
            else:
                res += " @{username}".format(username=username)
        return res
    elif message.sender_chat:
        user_id = message.sender_chat.id
        username = message.sender_chat.username
        title = message.sender_chat.title
        res = ""
        if title:
            res = "\"title\" "
        if username:
            if with_id:
                res += "@{username}({user_id}) (chat)".format(username=username, user_id=user_id)
            else:
                res += "@{username} (chat)".format(username=username, user_id=user_id)
        else:
            first_name = message.sender_chat.first_name
            last_name = message.sender_chat.last_name
            res = ""
            if first_name:
                res += first_name
                if last_name:
                    res += " {}".format(last_name)
            return "{}({}) (chat)".format(res, user_id)


def get_chat_by_msg(update):
    chat = update.effective_chat
    chat_id = chat.id
    title = chat.title
    username = chat.username
    res = ""
    if username:
        res += "@{} ".format(username)
    if title:
        res += "{}".format(title)
    if not (title or username):
        res = chat_id
    return res

