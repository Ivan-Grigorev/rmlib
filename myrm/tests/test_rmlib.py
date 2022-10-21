"""Module tests sample_foo function from rmlib.py"""

from myrm.rmlib import sample_foo


def test_sample_foo():
    """Function tests useful dict update"""
    result = sample_foo()
    result.update({"key_2": 2})
    assert len(result) == 2
    assert result["key_2"] == 2
