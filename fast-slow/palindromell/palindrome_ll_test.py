import pytest
from palindrome_ll import *
from linked_list import LinkedList

@pytest.mark.parametrize("input,expected", [([1,2,3,2,1], True), ([4,7,9,5,4], False), ([2,3,5,5,3,2], True), ([6,1,0,5,1,6], False)])
def test_palindrome(input, expected):
    ll = LinkedList()
    ll.create_linked_list(input)
    assert palindrome(ll) == expected

