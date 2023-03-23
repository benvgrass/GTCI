from linked_list import LinkedList

def palindrome(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    second_half = LinkedList.reverse_linked_list(slow)
    first_half = head
    slow.next = None

    while second_half is not None:
        if first_half.data != second_half.data: 
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True
