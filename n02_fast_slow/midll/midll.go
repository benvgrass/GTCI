package main

// getMiddleNode function to find the middle node of the linked list
func getMiddleNode(head *EduLinkedListNode) *EduLinkedListNode {
	slow := head
	fast := head

	for fast != nil && fast.next != nil {
		slow = slow.next
		fast = fast.next.next
	}
	return slow
}
