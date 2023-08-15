from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reverse(head):
    previous = None
    current = head
    while current:
        current.next = previous
        previous = current
        current = current.next

    return current