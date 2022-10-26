"""Module tests functions from rmlib.py"""

import os

from myrm.rmlib import mkdir, mv, mvdir, rm, rmdir


def test_mv(mv_example):
    """Tests mv() function"""
    mv(mv_example[0], mv_example[1])
    assert os.path.exists(mv_example[1] + mv_example[2]) == True
    assert os.path.exists(mv_example[0] + mv_example[2]) == False


def test_mvdir(mvdir_example):
    """Tests mvdir() function"""
    src_files = len(os.listdir(mvdir_example[0]))
    src_folder = os.path.basename(os.path.dirname(mvdir_example[0]))
    mvdir(mvdir_example[0], mvdir_example[1])
    assert os.path.exists(mvdir_example[0]) == False
    assert os.path.exists(mvdir_example[1]) == True
    assert src_files == len(os.listdir(mvdir_example[1] + src_folder))


def test_rm(rm_example):
    """Tests rm() function"""
    rm(rm_example)
    assert os.path.exists(rm_example) == False


def test_rmdir(rmdir_example):
    """Tests rmdir() function"""
    rmdir(rmdir_example)
    assert os.path.exists(rmdir_example) == False


def test_mkdir(mkdir_example):
    """Tests mkdir() function"""
    mkdir(mkdir_example)
    assert os.path.exists(mkdir_example) == True
