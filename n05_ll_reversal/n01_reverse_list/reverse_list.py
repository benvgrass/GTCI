from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reverse(head):
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous
