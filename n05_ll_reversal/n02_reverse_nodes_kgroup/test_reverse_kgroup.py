from linked_list import LinkedList, linked_list_to_list
from n05_ll_reversal.n02_reverse_nodes_kgroup.reverse_kgroup import reverse_k_groups
import pytest


@pytest.mark.parametrize("lst,k,expected", ([
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ([3, 4, 5, 6, 2, 8, 7, 7], 3, [5, 4, 3, 8, 2, 6, 7, 7]),
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5, 6, 7], 3, [3, 2, 1, 6, 5, 4, 7]),
    ([1, 2, 3, 4, 5, 6, 7], 7, [7, 6, 5, 4, 3, 2, 1])
]))
def test_reverse_k_groups(lst, k, expected):
    ll = LinkedList()
    ll.create_linked_list(lst)
    result_node = reverse_k_groups(ll.head, k)
    result_ll = LinkedList()
    result_ll.insert_node_at_head(result_node)
    result_lst = linked_list_to_list(result_ll)
    assert result_lst == expected
