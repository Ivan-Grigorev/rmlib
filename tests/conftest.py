import os

import pytest


@pytest.fixture
def my_example(fs):
    src = "src"
    dst = "dst"
    file = "traveler.txt"

    fs.create_dir(src)
    fs.create_dir(dst)
    fs.create_file(os.path.join(src, file))
    return src, dst, file
