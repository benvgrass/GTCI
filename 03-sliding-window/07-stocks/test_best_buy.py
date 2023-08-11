import pytest
from best_buy import max_profit


@pytest.mark.parametrize("prices, expected", [
    ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9], 9),
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([2, 6, 8, 7, 8, 7, 9, 4, 1, 2, 4, 5, 8], 7),
    ([1, 4, 2], 1)
])
def test_max_profit(prices, expected):
    assert max_profit(prices) == expected
