"""Module move, remove directories and files"""

import os


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
        print(error)


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
        print(error)


def rm(path):
    """Function remove files"""
    try:
        os.remove(path)
        print(f"{path} removed successfully.")
    except OSError as error:
        print(error)


def rmdir(path):
    """Function remove directories"""
    try:
        os.rmdir(path)
        print(f"{path} successfully removed.")
    except OSError as error:
        print(error)


def mkdir(path):
    """Function create directories"""
    try:
        os.mkdir(path)
        print(f"{path} successfully created.")
    except OSError as error:
        print(error)
