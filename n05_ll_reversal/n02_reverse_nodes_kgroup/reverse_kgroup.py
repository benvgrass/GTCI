from n05_ll_reversal.n01_reverse_list.reverse_list import reverse_linked_list


def reverse_k_groups(head, k):
    new_group_head = traverse_to_depth_k(head, k)
    if new_group_head:
        next_group = new_group_head.next
        new_group_head.next = None
        reverse_linked_list(head)
        head.next = reverse_k_groups(next_group, k)
        return new_group_head
    return head


def traverse_to_depth_k(head, k):
    new_head = head
    count = 1
    while count < k and new_head:
        new_head = new_head.next
        count += 1

    return new_head
