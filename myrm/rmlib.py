"""Module move, remove directories and files"""

import errno
import logging
import os
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def mv(src, dst):
    """Function move files"""
    try:
        os.rename(src, dst)
        logger.info("File by path %s was successfully moved.", src)
    except OSError as err:
        if err.errno == errno.EEXIST:
            logger.error("By this path file already exists.")
        else:
            sys.exit(err.strerror)


def mvdir(src, dst):
    """Function move directories"""
    move_to = os.path.join(dst, os.path.basename(src))
    try:
        mkdir(move_to)
        all_files = os.listdir(src)
        for file in all_files:
            mv(os.path.join(src, file), os.path.join(move_to, file))
        rmdir(src)
        logger.info("Directory by path %s was successfully moved.", src)
    except OSError as err:
        if err.errno == errno.ENOENT:
            logger.error("No such file or directory.")
        else:
            sys.exit(err.strerror)


def rm(path):
    """Function remove files"""
    try:
        os.remove(path)
        logger.info("File by path %s was successfully moved.", path)
    except OSError as err:
        if err.errno == errno.ENOENT:
            logger.error("No such file or directory.")
        else:
            sys.exit(err.strerror)


def rmdir(path):
    """Function remove directories"""
    try:
        if os.path.islink(path):
            os.unlink(path)
        if os.listdir(path):
            for root, dirs, files in os.walk(path, topdown=False):
                for name in files:
                    rm(os.path.join(root, name))
                os.removedirs(root)
            logger.info("Directory by path %s was successfully removed.", path)
        else:
            os.removedirs(path)
    except OSError as err:
        if err.errno == errno.ENOENT:
            logger.error("No such file or directory.")
        else:
            sys.exit(err.strerror)


def mkdir(path):
    """Function create directories"""
    try:
        os.makedirs(path)
        logger.info("Directory by path %s was successfully created.", path)
    except OSError as err:
        if err.errno == errno.EEXIST:
            logger.error("By this path directory already exists.")
        else:
            sys.exit(err.strerror)
