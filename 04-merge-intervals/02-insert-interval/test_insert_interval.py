import pytest
from insert_interval import insert_interval, Interval


@pytest.mark.parametrize("intervals, new_interval, expected", [
    ([[1, 2], [3, 4], [5, 8], [9, 15]], [2, 5], [[1, 8], [9, 15]]),
    ([[1, 6], [8, 9], [10, 15], [16, 18]], [9, 10], [[1, 6], [8, 15], [16, 18]]),
    ([[1, 2], [3, 4], [5, 8], [9, 15]], [16, 17], [[1, 2], [3, 4], [5, 8], [9, 15], [16, 17]]),
    ([[1, 4], [5, 6], [7, 8], [9, 10]], [1, 5], [[1, 6], [7, 8], [9, 10]]),
    ([[1, 3], [4, 6], [7, 8], [9, 10]], [1, 10], [[1, 10]])

])
def test_insert_interval(intervals, new_interval, expected):
    assert insert_interval([Interval(x[0], x[1]) for x in intervals],
                           Interval(new_interval[0], new_interval[1]) ==
                           [Interval(e[0], e[1]) for e in expected])
