import pytest
from min_sub_sum import min_sub_array_len


# noinspection SpellCheckingInspection
@pytest.mark.parametrize("t,nums,expected", [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (4, [1, 4, 4], 1),
    (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),
    (10, [1, 2, 3, 4], 4),
    (5, [1, 2, 1, 3], 3)
])
def test_min_sub_array_len(t, nums, expected):
    assert min_sub_array_len(t, nums) == expected