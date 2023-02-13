package main

func detectCycle(head *EduLinkedListNode) bool {
	slow := head
	fast := head

	for fast != nil {
		slow = slow.next
		fast = fast.next.next

		if slow == fast {
			return true
		}
	}
	return false
}
