import pytest
from intersections import intervals_intersection, Interval


@pytest.mark.parametrize("a,b,expected", [
    ([[1, 4], [5, 6], [7, 8], [9, 15]],
     [[2, 4], [5, 7], [9, 15]],
     [[2, 4], [5, 6], [7, 7], [9, 15]]),
    ([[1, 3], [4, 6], [8, 10], [11, 15]],
     [[2, 3], [10, 15]],
     [[2, 3], [10, 10], [11, 15]]),
    ([[1, 2], [4, 6], [7, 8], [9, 10]],
     [[3, 6], [7, 8], [9, 10]],
     [[4, 6], [7, 8], [9, 10]]),
    ([[1, 3], [5, 6], [7, 8], [9, 10], [12, 15]],
     [[2, 4], [7, 10]],
     [[2, 3], [7, 8], [9, 10]]),
    ([[1, 2]],
     [[1, 2]],
     [[1, 2]])

])
def test_intervals_intersection(a, b, expected):
    assert unpack_interval_list(
        intervals_intersection(make_interval_list(a),
                               make_interval_list(b))) == expected


def make_interval_list(l):
    return [Interval(x[0], x[1]) for x in l]


def unpack_interval_list(l):
    return [[x.start, x.end] for x in l]
