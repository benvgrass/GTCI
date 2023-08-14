package main

import (
	"fmt"
	"testing"
)

func TestCircularArrayLoop(t *testing.T) {
	tests := []struct {
		input    []int
		expected bool
	}{
		{[]int{1, 3, -2, -4, 1}, true},
		{[]int{2, 1, -1, -2}, false},
		{[]int{1, 3, -2, -4, 1}, true},
		{[]int{3, 2, 1, 1, -4, 1}, false},
		{[]int{1, 2, -3, 3, 4, 7, 1}, true},
		{[]int{3, 3, 1, -1, 2}, true},
	}

	for i, testCase := range tests {
		t.Run(fmt.Sprintf("CircularArrayLoop-%d", i), func(t *testing.T) {
			actual := circularArrayLoop(testCase.input)
			if actual != testCase.expected {
				t.Errorf("input: %v; expected: %v, actual: %v", testCase.input, testCase.expected, actual)
			} else {
				t.Logf("Pass!")
			}
		})
	}

}

/*






 */
