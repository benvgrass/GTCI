import pytest
from merge_intervals import merge_intervals


@pytest.mark.parametrize("intervals, expected", [
    # TODO add test cases
])
def test_merge_intervals(intervals, expected):
    assert merge_intervals(intervals) == expected
