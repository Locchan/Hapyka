from time import time
import os
from hapyka.utils.logger import get_logger
from __main__ import config_provider

last_repost = 0
logger = get_logger()
reposter_dir = config_provider.get("reposter/directory")


def get_pics_to_repost():
    return [f for f in os.listdir(reposter_dir) if ".png" in f]


def reposter_repost_picture(update, context):
    global last_repost
    if time() - last_repost < 3600:
        return
    pics_to_repost = get_pics_to_repost()
    logger.info("There are {} pictures in queue for reposting".format(len(pics_to_repost)))
    if len(pics_to_repost) > 0:
        apicture_path = os.path.join(reposter_dir, pics_to_repost[0])
        apicture_path_txt = apicture_path[:-4] + ".txt"
        if not os.path.exists(apicture_path_txt):
            logger.warning("Caption file for {} does not exist. Will not repost the picture.".format(apicture_path))
            os.remove(apicture_path)
            return
        else:
            with open(apicture_path_txt, "r") as caption_file:
                lines = caption_file.readlines()
                chat = lines[0]
                caption = "\n".join(lines[1:])
        context.bot.send_photo(chat, photo=open(apicture_path, "rb"), caption=caption)
        logger.info("Reposting {}...".format(pics_to_repost[0]))
        os.remove(apicture_path)
        os.remove(apicture_path_txt)
        last_repost = time()
    else:
        logger.info("No pictures to repost.")