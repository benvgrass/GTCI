package main

import "testing"

type DetectCycleTestPair struct {
	input    *EduLinkedListNode
	expected bool
}

func TestDetectCycle(t *testing.T) {

}

func createTestPair(list []int, cycle int) DetectCycleTestPair {
	ll := new(EduLinkedList)
	var lastNode EduLinkedListNode
	for i := len(list) - 1; i >= 0; i-- {
		newNode := InitLinkedListNode(list[i])
		ll.InsertNodeAtHead(newNode)
		if i == len(list)-1 {
			lastNode = *newNode
		}
		if i == cycle {
			lastNode.next = newNode
		}
	}

	var containsCycle bool
	if cycle >= 0 {
		containsCycle = true
	}
	return DetectCycleTestPair{ll.head, containsCycle}

}
