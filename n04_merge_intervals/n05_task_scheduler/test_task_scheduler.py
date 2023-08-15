from task_scheduler import least_time
import pytest


@pytest.mark.parametrize("tasks,expected", [

])
def test_least_time(tasks, expected):
    assert least_time(tasks) == expected
