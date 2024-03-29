import pytest
from palindrome_ll import *
from linked_list import LinkedList


@pytest.mark.parametrize("test_input,expected",
                         [([1, 2, 3, 2, 1], True), ([4, 7, 9, 5, 4], False), ([2, 3, 5, 5, 3, 2], True),
                          ([6, 1, 0, 5, 1, 6], False)])
def test_palindrome(test_input, expected):
    ll = LinkedList()
    ll.create_linked_list(test_input)
    assert palindrome(ll.head) == expected
