from linked_list_node import LinkedListNode
from n05_ll_reversal.n01_reverse_list.reverse_list import reverse_linked_list
from n05_ll_reversal.n02_reverse_nodes_kgroup.reverse_kgroup import traverse_to_depth_k


def reverse_between(head, left, right):
    left_node = traverse_to_depth_k(head, left)
    right_node = traverse_to_depth_k(head, right)
    resume_node = right_node.next
    right_node.next = None
    reverse_linked_list(left_node)
    left_node.next = resume_node
    if left > 1:
        pause_node = traverse_to_depth_k(head, left - 1)
        pause_node.next = right_node
    else:
        head = right

    return head
