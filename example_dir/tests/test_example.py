"""Module tests sample_foo function from example.py"""

from example_dir.example import sample_foo


def test_sample_foo():
    """Function tests useful dict update"""
    result = sample_foo()
    result.update({"key_2": 2})
    assert len(result) == 2
    assert result["key_2"] == 2
