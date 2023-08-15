from linked_list import LinkedList, linked_list_to_list
from n05_ll_reversal.n02_reverse_nodes_kgroup.reverse_kgroup import reverse_k_groups
import pytest

@pytest.mark.parametrize("lst,k,expected", ([

]))
def test_reverse_k_groups(lst,k,expected):
    ll = LinkedList()
    ll.create_linked_list(lst)
    result = linked_list_to_list(reverse_k_groups(ll.head, k))
    assert result == expected
