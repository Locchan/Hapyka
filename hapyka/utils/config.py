import argparse
import __main__
import locred.containers

from hapyka.utils.logger import get_logger
from locred.LoCred import LoCred

logger = get_logger()

try:

    config_args = {}
    args_parser = argparse.ArgumentParser(description='Hapyka. Python reimplementation of Haruka bot.')
    args_parser.add_argument('--config_type', required=True, type=str,
                             help='Credential storage to use. Provided by LoCred'.format(
                                 list(locred.containers.container_types.keys())))
    args_parser.add_argument('--config_arg', required=True, action='append', nargs='+',
                             help='Additional arguments that will be passed to LoCred. '
                                  'Each parameter\'s key and value are provided separately.'
                                  'Example: --config_arg testkey1 testval1 --config_arg testkey2 testval2')
    args = args_parser.parse_args()

    for anentry in args.config_arg:
        config_args[anentry[0]] = anentry[1]

    config_container = LoCred(args.config_type, **config_args)
    __main__.config_container = config_container
except Exception as e:
    logger.error("Incorrect arguments. Error: {}".format(e.__class__.__name__))
    exit(1)
