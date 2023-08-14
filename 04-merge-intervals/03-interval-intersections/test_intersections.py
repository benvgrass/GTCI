import pytest
from intersections import intervals_intersection, Interval


@pytest.mark.parametrize("a,b,expected", [
    ([[1,4],[5,6],[7,8],[9,15]],
     [[2,4],[5,7],[9,15]],
     [[2,4],[5,6],[7,7],[9,15]]),

])
def test_intervals_intersection(a, b, expected):
    assert intervals_intersection(make_interval_list(a),
                                  make_interval_list(b)) == make_interval_list(expected)


def make_interval_list(l):
    return [Interval(x[0], x[1]) for x in l]
