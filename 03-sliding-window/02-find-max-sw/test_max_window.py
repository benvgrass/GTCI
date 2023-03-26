import pytest
from max_window import find_max_sliding_window


@pytest.mark.parametrize("nums,w,expected",
                         [
                             ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, [3, 4, 5, 6, 7, 8, 9, 10]),
                             ([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 4, [3, 3, 3, 3, 3, 3, 3]),
                             ([10, 6, 9, -3, 23, -1, 34, 56, 67, -1, -4, -8, -2, 9, 10, 34, 67], 2,
                              [10, 9, 9, 23, 35, 56, 67, 67, -1, -4, -2, 9, 10, 34, 67]),
                             ([4, 5, 6, 1, 2, 3], 1, [4, 5, 6, 1, 2, 3]),
                             ([9, 5, 3, 1, 6, 3], 2, [9, 5, 3, 6, 6]),
                             ([1, 2], 2, [2])
                         ])
def test_find_max_sliding_window(nums, w, expected):
    assert find_max_sliding_window(nums, w) == expected
