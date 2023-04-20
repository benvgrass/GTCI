import pytest
from min_substring import min_substring


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("s,t,expected", [
    ("ABC", "ABCD", "ABC"),
    ("XYZYX", "XYZ", "XYZ"),
    ("ABXYZJKLSNFC", "ABC", "ABXYZJKLSNFC"),
    ("AAAAAAAAAAA", "A", "A"),
    ("ABDFGDCKAB", "ABCD", "DCKAB")
])
def test_min_substring(s, t, expected):
    assert min_substring(s, t) == expected
