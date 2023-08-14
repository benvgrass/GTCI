import pytest
from free_time import employee_free_time
from n04_merge_intervals.interval import make_interval_list, unpack_interval_list


@pytest.mark.parametrize("s, expected", [

])
def test_employee_free_time(s, expected):
    assert map(unpack_interval_list,
               employee_free_time(map(make_interval_list, s))) == expected
