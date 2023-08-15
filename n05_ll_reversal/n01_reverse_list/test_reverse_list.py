import pytest
from n05_ll_reversal.n01_reverse_list.reverse_list import reverse_linked_list
from linked_list import LinkedList, linked_list_to_list


@pytest.mark.parametrize("lst", ([
    [1, -2, 3, 4, -5, 4, 3, -2, 1],
    [-1, -5, -3, -7, -8, -6, -2],
    [-1, 2, -3, 4],
    [1, -1, -2, 3, -4, 5],
    [28, 21, 14, 7]
]))
def test_reverse(lst):
    ll = LinkedList()
    ll.create_linked_list(lst)
    reversed_ll = LinkedList()
    reversed_ll.insert_node_at_head(reverse_linked_list(ll.head))
    assert linked_list_to_list(reversed_ll) == lst.reverse()
