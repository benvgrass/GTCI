package main

import (
	"fmt"
	"testing"
)

func TestGetMiddleNode(t *testing.T) {
	tests := []struct {
		input    []int
		expected int
	}{
		{[]int{1, 2, 3, 4, 5}, 3},
		{[]int{1, 2, 3, 4, 5, 6}, 4},
		{[]int{3, 2, 1}, 2},
		{[]int{10}, 10},
		{[]int{1, 2}, 2},
	}

	for i, testCase := range tests {
		t.Run(fmt.Sprintf("GetMiddleNode-%d", i), func(t *testing.T) {
			inputList := new(EduLinkedList)
			inputList.CreateLinkedList(testCase.input)
			actual := getMiddleNode(inputList.head)
			if actual.data != testCase.expected {
				t.Fatalf("input: %v; expected: %v, actual %v", testCase.input, testCase.expected, actual.data)
			} else {
				t.Logf("Pass!")
			}
		})
	}
}
