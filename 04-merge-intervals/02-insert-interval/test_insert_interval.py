import pytest
from insert_interval import insert_interval, Interval


@pytest.mark.parametrize("intervals, new_interval, expected", [

])
def test_insert_interval(intervals, new_interval, expected):
    assert insert_interval([Interval(x[0], x[1]) for x in intervals],
                           Interval(new_interval[0], new_interval[1]) ==
                           [Interval(e[0], e[1]) for e in expected])
