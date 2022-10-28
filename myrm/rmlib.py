"""Module move, remove directories and files"""

import errno
import logging
import logging.config
import os
import sys

# logging.basicConfig(
#     format="%(asctime)s - %(levelname)s :: %(name)s :: %(message)s",
#     datefmt="%Y-%m-%d--%H-%M-%S",
# )
# logging.config.dictConfig({
#
# })
logger = logging.getLogger("rmlib")


def mv(src, dst):
    """Function move files"""
    try:
        os.rename(src, dst)
    except OSError:  # as err:
        logger.error("Message from mv")
        # sys.exit()


def mvdir(src, dst):
    """Function move folders"""
    try:  # try only ...
        move_to = os.path.join(dst, os.path.basename(os.path.dirname(src)))
        mkdir(move_to)
        all_files = os.listdir(src)  # if folders inside
        for file in all_files:
            os.rename(os.path.join(src, file), os.path.join(move_to, file))
        rmdir(src)
    except OSError:  # as err:
        logger.error("Message from mvdir")
        # sys.exit()


def rm(path):
    """Function remove files"""
    try:
        os.remove(path)
    except OSError:  # as err:
        logger.info("Message from rm")
        # sys.exit()


def rmdir(path):
    """Function remove directories"""
    try:
        if os.path.islink(path):
            os.unlink(path)
        elif os.listdir(path):
            for file in os.listdir(path):
                os.remove(os.path.join(path, file))
            os.removedirs(path)
        else:
            os.removedirs(path)
    except OSError:  # as err:
        logger.error("Message from rmdir")
        # sys.exit()


def mkdir(path):
    """Function create directories"""
    try:
        os.makedirs(path)
    except OSError as err:
        if err.errno == errno.EEXIST:
            logger.error("By this path directory already exists.")
        else:
            sys.exit(err.errno)


def main():
    pass


# if __name__ == '__main__':
#     main()
