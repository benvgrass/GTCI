import pytest
from longest_substring import find_longest_substring


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("input_str,expected", [
    ("abcdbea", 5),
    ("aba", 2),
    ("abccabcabcc", 3),
    ("aaaabaaa", 2),
    ("bbbbb", 1)
])
def test_find_longest_substring(input_str, expected):
    assert find_longest_substring(input_str) == expected