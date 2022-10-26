import pytest


@pytest.fixture
def mv_example():
    src = "/Users/ivangrigorev/documents/src/"
    dst = "/Users/ivangrigorev/documents/dst/"
    file = "traveler.txt"
    return [src, dst, file]


@pytest.fixture
def mvdir_example():
    src = "/Users/ivangrigorev/documents/src/"
    dst = "/Users/ivangrigorev/documents/dst/"
    return [src, dst]


@pytest.fixture
def rm_example():
    src = "/Users/ivangrigorev/documents/src/traveler.txt"
    return src


@pytest.fixture
def rmdir_example():
    dst = "/Users/ivangrigorev/documents/new/"
    return dst


@pytest.fixture
def mkdir_example():
    dst = "/Users/ivangrigorev/documents/new/"
    return dst
