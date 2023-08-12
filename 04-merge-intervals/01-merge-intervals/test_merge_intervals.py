import pytest
from merge_intervals import merge_intervals
from merge_intervals import Interval


@pytest.mark.parametrize("intervals, expected", [
    ([Interval(1, 5), Interval(3, 7), Interval(4, 6)], [Interval(1, 7)]),
    ([Interval(1, 5), Interval(4, 6), Interval(6, 8), Interval(11, 15)], [Interval(1, 8), Interval(11, 15)]),
    ([Interval(1, 5)], [Interval(1, 5)]),
    ([Interval(1, 9), Interval(3, 8), Interval(4, 4)], [Interval(1, 9)]),
    ([Interval(1, 2), Interval(3, 4), Interval(8, 8)], [Interval(1, 2), Interval(3, 4), Interval(8, 8)])
])
def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected
