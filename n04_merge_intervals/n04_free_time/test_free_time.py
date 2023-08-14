import pytest
from free_time import employee_free_time
from n04_merge_intervals.interval import make_interval_list, unpack_interval_list


@pytest.mark.parametrize("s, expected", [
    ([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]], [[3, 4]]),
    ([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]], [[5, 6], [7, 9]]),
    ([[[2, 3], [7, 9]], [[1, 4], [6, 7]]], [[4, 6]]),
    ([[[3, 5], [8, 10]], [[4, 6], [9, 12]], [[5, 6], [8, 10]]], [[6, 8]]),
    ([[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]], [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]],
      [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]], [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]],
     [[2, 3], [4, 5], [6, 7], [8, 9], [10, 11]])
])
def test_employee_free_time(s, expected):
    assert unpack_interval_list(employee_free_time(map(make_interval_list, s))) == expected
