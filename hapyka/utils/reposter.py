import random
from time import time
import os
from hapyka.utils.logger import get_logger
from __main__ import config_provider

reposter_speed_default = 3600
reposter_speed_max = 600

# Reposter speed increases by reposter_speed_increase for every reposter_speed_rate pictures in the queue
reposter_speed_rate = 5
reposter_speed_increase = 180
reposter_speed_start = 48
reposter_speed = 0

last_repost = time()
logger = get_logger()
reposter_dir = config_provider.get("reposter/directory")


def get_pics_to_repost():
    return [f for f in os.listdir(reposter_dir) if ".png" in f]


def calculate_reposter_speed(pics_to_repost=None):
    if pics_to_repost is None:
        pics_to_repost = get_pics_to_repost()
    queue_length = len(pics_to_repost)
    if queue_length < reposter_speed_start:
        return reposter_speed_default
    queue_length = queue_length - reposter_speed_start
    speed = reposter_speed_default - (reposter_speed_increase * int(queue_length / reposter_speed_rate))
    if speed < reposter_speed_max:
        return reposter_speed_max
    return speed


def get_reposter_status():
    pics_to_repost = get_pics_to_repost()
    return (calculate_reposter_speed(pics_to_repost), len(pics_to_repost), reposter_speed_start, reposter_speed_rate,
            reposter_speed_increase, reposter_speed_default, reposter_speed_max)


def reposter_repost_picture(update, context):
    global last_repost, reposter_speed
    if time() - last_repost < reposter_speed:
        return
    pics_to_repost = get_pics_to_repost()
    reposter_speed = calculate_reposter_speed(pics_to_repost)
    logger.info("There are {} pictures in queue for reposting".format(len(pics_to_repost)))
    if len(pics_to_repost) > 0:
        random_pic = random.choice(pics_to_repost)
        apicture_path = os.path.join(reposter_dir, random_pic)
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
        logger.info("Reposting {}...".format(random_pic))
        os.remove(apicture_path)
        os.remove(apicture_path_txt)
        last_repost = time()
    else:
        logger.info("No pictures to repost.")
