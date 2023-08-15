from n04_merge_intervals.n05_task_scheduler.task_scheduler import least_time
import pytest


@pytest.mark.parametrize("tasks, n,expected", [
    ([["A", "A", "B", "B"] , 2,5]),
    ([["A", "A", "A", "B", "B", "C", "C"], 1,7]),
    ([["S", "I", "V", "U", "W", "D", "U", "X"] , 0,8]),
    ([["A", "K", "X", "M", "W", "D", "X", "B", "D", "C", "O", "Z", "D", "E", "Q"] , 3,15]),
    ([["A", "B", "C", "O", "Q", "C", "Z", "O", "X", "C", "W", "Q", "Z", "B", "M", "N", "R", "L", "C", "J"],
      10, 34])
])
def test_least_time(tasks, n, expected):
    assert least_time(tasks, n) == expected
