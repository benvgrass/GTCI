import pytest

from linked_list import LinkedList, linked_list_to_list
from n05_ll_reversal.n03_reverse_list_2.reverse_list_2 import reverse_between


@pytest.mark.parametrize("lst,l,r,expected", [

])
def test_reverse_between(lst, l, r, expected):
    assert linked_list_to_list(reverse_between(LinkedList.from_list(lst), l, r)) == expected
