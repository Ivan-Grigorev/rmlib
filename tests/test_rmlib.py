"""Module tests functions from rmlib.py"""

import os

from myrm.rmlib import mkdir, mv, mvdir, rm, rmdir


def test_mv(my_example):
    """Tests mv() function"""
    move_from = os.path.join(my_example[0], my_example[2])
    move_to = os.path.join(my_example[1], my_example[2])
    mv(move_from, move_to)
    assert os.path.exists(move_from) == False
    assert os.path.exists(move_to) == True


def test_mvdir(my_example):
    """Tests mvdir() function"""
    src_files = len(os.listdir(my_example[0]))
    src_folder = os.path.basename(os.path.dirname(my_example[0]))
    mvdir(my_example[0], my_example[1])
    assert os.path.exists(my_example[0]) == False
    assert os.path.exists(my_example[1]) == True
    assert src_files == len(os.listdir(os.path.join(my_example[1], src_folder)))


def test_rm(my_example):
    """Tests rm() function"""
    rm(my_example[2])
    assert os.path.exists(my_example[2]) == False


def test_rmdir(my_example):
    """Tests rmdir() function"""
    rmdir(my_example[0])
    assert os.path.exists(my_example[0]) == False


def test_mkdir(my_example):
    """Tests mkdir() function"""
    mkdir(my_example[1])
    assert os.path.exists(my_example[1]) == True
