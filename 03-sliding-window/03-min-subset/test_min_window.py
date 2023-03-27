import pytest
from min_window import min_window


@pytest.mark.parametrize("s1,s2,expected",
                         [
                             ('abcdebdde', 'bde', 'bcde'),
                             ('fgrqsqsnodwmxzkzxwqegkndaa', 'kzed', 'kzxwqegknd'),
                             ('michmznaitnjdnjkdsnmichmznait', 'michmznait', 'michmznait'),
                             ('afgegrwgwga', 'aa', 'afgegrwgwga'),
                             ('abababa', 'ba', 'ba')
                         ])
def test_min_window(s1, s2, expected):
    assert min_window(s1, s2) == expected
