package main

import (
	"fmt"
	"testing"
)

type DetectCycleTestPair struct {
	input    *EduLinkedListNode
	expected bool
}

func TestDetectCycle(t *testing.T) {
	tests := []DetectCycleTestPair{
		createTestPair([]int{2, 4, 6, 8, 10}, 2),
		createTestPair([]int{1, 3, 5, 7, 9}, -1),
		createTestPair([]int{1, 2, 3, 4, 5}, 3),
		createTestPair([]int{0, 2, 3, 5, 6}, -1),
		createTestPair([]int{3, 6, 9, 10, 11}, 0),
	}

	for i, testCase := range tests {
		t.Run(fmt.Sprintf("DetectCycle-%d", i), func(t *testing.T) {
			actual := detectCycle(testCase.input)
			if actual != testCase.expected {
				t.Fatalf("expected: %v, actual %v", testCase.expected, actual)
			} else {
				t.Logf("Pass!")
			}
		})
	}
}

func createTestPair(list []int, cycle int) DetectCycleTestPair {
	ll := new(EduLinkedList)
	var lastNode *EduLinkedListNode
	for i := len(list) - 1; i >= 0; i-- {
		newNode := InitLinkedListNode(list[i])
		if i == len(list)-1 {
			lastNode = newNode
		}
		if i == cycle {
			lastNode.next = newNode
		}
		ll.InsertNodeAtHead(newNode)

	}

	var containsCycle bool
	if cycle >= 0 {
		containsCycle = true
	}
	return DetectCycleTestPair{ll.head, containsCycle}

}
