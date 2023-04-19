import random
from time import time
import os
from hapyka.utils.logger import get_logger
from __main__ import config_provider

reposter_speed_default = 3600
reposter_speed_max = 600

# Reposter speed increases by reposter_speed_increase for every reposter_speed_rate pictures over reposter_speed_start
#  in the queue
reposter_config = {
    "reposter_speed_rate": 0,
    "reposter_speed_increase": 0,
    "reposter_speed_start": 0,
    "reposter_speed": 0,
    "reposter_configured": False
}

last_repost = time()
logger = get_logger()
reposter_dir = config_provider.get("reposter/directory")


def get_reposter_config():
    global reposter_config
    from __main__ import config_provider
    logger.info("RP: Loading configuration...")
    reposter_config["reposter_speed_rate"] = config_provider.get("reposter_speed_rate")
    reposter_config["reposter_speed_increase"] = config_provider.get("reposter_speed_increase")
    reposter_config["reposter_speed_start"] = config_provider.get("reposter_speed_start")
    reposter_config["reposter_configured"] = True


def require_reposter_config(func):
    def internal(*args, **kwargs):
        if not reposter_config["reposter_configured"]:
            get_reposter_config()
        return func(args, kwargs)
    return internal


def get_pics_to_repost():
    return [f for f in os.listdir(reposter_dir) if ".png" in f]


@require_reposter_config
def calculate_reposter_speed(args, kwargs):
    pics_to_repost=args[0]
    if pics_to_repost is None:
        pics_to_repost = get_pics_to_repost()
    queue_length = len(pics_to_repost)
    if queue_length < reposter_config["reposter_speed_start"]:
        return reposter_speed_default
    queue_length = queue_length - reposter_config["reposter_speed_start"]
    speed = reposter_speed_default - (reposter_config["reposter_speed_increase"] *
                                      int(queue_length / reposter_config["reposter_speed_rate"]))
    if speed < reposter_speed_max:
        return reposter_speed_max
    return speed


@require_reposter_config
def get_reposter_status(args, kwargs):
    pics_to_repost = get_pics_to_repost()
    return (calculate_reposter_speed(pics_to_repost), len(pics_to_repost), reposter_config["reposter_speed_start"],
            reposter_config["reposter_speed_rate"],  reposter_config["reposter_speed_increase"], reposter_speed_default,
            reposter_speed_max)


@require_reposter_config
def reposter_repost_picture(args, kwargs):
    from __main__ import hapyka
    global last_repost, reposter_config
    passed_time = time() - last_repost
    if passed_time < reposter_config["reposter_speed"]:
        logger.debug("RP: Not reposting. {} (rounded) secs passed. {} secs needed."
                     .format(int(passed_time), reposter_config["reposter_speed"]))
        return
    pics_to_repost = get_pics_to_repost()
    reposter_config["reposter_speed"] = calculate_reposter_speed(pics_to_repost)
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
        hapyka.bot.send_photo(chat, photo=open(apicture_path, "rb"), caption=caption)
        logger.info("Reposting {}...".format(random_pic))
        os.remove(apicture_path)
        os.remove(apicture_path_txt)
        last_repost = time()
    else:
        logger.debug("RP: No pictures to repost.")
