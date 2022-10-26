"""Module move, remove directories and files"""

import logging
import os

logging.basicConfig(
    filename="/Users/ivangrigorev/documents/rmlib/rmlib.log",
    format="%(asctime)s - %(levelname)s :: %(name)s :: %(message)s",
    datefmt="%Y-%m-%d--%H-%M-%S",
)
logger = logging.getLogger()


def mv(src, dst):
    """Function move files"""
    try:
        if os.path.isdir(src):
            print(f"{src} is directory.")
        elif os.path.exists(dst):
            print(f"File exists in this folder '{dst}'")
        else:
            os.replace(src, dst)
            print("File successfully moved.")
    except OSError as error:
        logger.error(error)


def mvdir(src, dst):
    """Function move folders"""
    try:
        move_to = dst + os.path.basename(os.path.dirname(src))
        os.mkdir(move_to)
        all_files = os.listdir(src)
        for file in all_files:
            os.replace(src + file, move_to + "/" + file)
        os.rmdir(src)
        print("Directory successfully moved!")
    except OSError as error:
        logger.error(error)


def rm(path):
    """Function remove files"""
    try:
        os.remove(path)
        print(f"{path} removed successfully.")
    except OSError as error:
        logger.error(error)


def rmdir(path):
    """Function remove directories"""
    try:
        if os.listdir(path):
            for f in os.listdir(path):
                os.remove(path + f)
            os.rmdir(path)
        else:
            os.rmdir(path)
        print(f"{path} successfully removed.")
    except OSError as error:
        logger.error(error)


def mkdir(path):
    """Function create directories"""
    try:
        os.mkdir(path)
        print(f"{path} successfully created.")
    except OSError as error:
        logger.error(error)
