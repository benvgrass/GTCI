import pytest
from min_substring import min_window


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("s,t,expected", [
    ("ABCD", "ABC", "ABC"),
    ("XYZYX", "XYZ", "XYZ"),
    ("ABXYZJKLSNFC", "ABC", "ABXYZJKLSNFC"),
    ("AAAAAAAAAAA", "A", "A"),
    ("ABDFGDCKAB", "ABCD", "DCKAB")
])
def test_min_substring(s, t, expected):
    assert min_window(s, t) == expected
