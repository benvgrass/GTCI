import pytest

from linked_list import LinkedList
from n05_ll_reversal.n04_reorder_list.reorder_list import reorder_list


@pytest.mark.parametrize("lst,expected", [
    ([1, 1, 2, 2, 3, -1, 10, 12], [1, 12, 1, 10, 2, -1, 2, 3]),
    ([10, 20, -22, 21, -12], [10, -12, 20, 21, -22]),
    ([1, 3, 5, 7, 9, 10, 8, 6, 4, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
    ([7, 0, 10, 13, 12, 19, 1, 3, 6, 7, 4, 2, 11], [7, 11, 0, 2, 10, 4, 13, 7, 12, 6, 19, 3, 1])
])
def test_reorder_list(lst, expected):
    input_node = LinkedList.from_list(lst).head
    output_list = LinkedList.from_node(reorder_list(input_node)).to_list()
    assert output_list == expected
