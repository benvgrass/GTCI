import pytest
from n04_merge_intervals.n06_meeting_rooms.meeting_rooms import find_sets
from n04_merge_intervals.interval import make_interval_list


@pytest.mark.parametrize("meetings,expected", [
    ([[2, 8], [3, 4], [3, 9], [5, 11], [8, 20], [11, 15]], 3),
    ([[1, 3], [2, 6], [8, 10], [9, 15], [12, 14]], 2),
    ([[1, 2], [4, 6], [3, 4], [7, 8]], 1),
    ([[1, 7], [2, 6], [3, 7], [4, 8], [5, 8]], 5),
    ([[1, 2], [1, 2], [1, 2]], 3)
])
def test_find_sets(meetings, expected):
    assert find_sets(make_interval_list(meetings)) == expected
