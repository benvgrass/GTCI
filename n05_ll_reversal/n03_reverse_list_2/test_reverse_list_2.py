import pytest

from linked_list import LinkedList, linked_list_to_list
from n05_ll_reversal.n03_reverse_list_2.reverse_list_2 import reverse_between


@pytest.mark.parametrize("lst,l,r,expected", [
    ([1, 2, 3, 4, 5, 4, 3, 2, 1], 1, 9, [1, 2, 3, 4, 5, 4, 3, 2, 1]),
    ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
    ([103, 7, 10, -9, 105, 67, 31, 63], 1, 8, [63, 31, 67, 105, -9, 10, 7, 103]),
    ([-499, 399, -299, 199, -99, 9], 3, 5, [-499, 399, -99, 199, -299, 9]),
    ([7, -9, 2, -10, 1, -8, 6], 2, 5, [7, 1, -10, 2, -9, -8, 6])
])
def test_reverse_between(lst, l, r, expected):
    input_head = LinkedList.from_list(lst).head
    output_list = LinkedList.from_node(reverse_between(input_head, l, r))
    assert linked_list_to_list(output_list) == expected
