from linked_list_node import LinkedListNode
from n05_ll_reversal.n01_reverse_list.reverse_list import reverse_linked_list


def reorder_list(head):
    # find half-point
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid_point = slow.next
    slow.next = None

    # reverse second half
    head_1 = head
    head_2 = reverse_linked_list(mid_point)

    # merge both sides
    while head_2:
        next_head_1 = head_1.next
        next_head_2 = head_2.next
        head_2.next = next_head_1
        head_1.next = head_2

        head_1 = next_head_1
        head_2 = next_head_2

    return head
