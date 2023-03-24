package main

func detectCycle(head *EduLinkedListNode) bool {
	slow := head
	fast := head

	for fast != nil {
		slow = slow.next
		fast = fast.next
		if fast != nil {
			fast = fast.next
		}

		if slow == fast {
			return true
		}
	}
	return false
}
