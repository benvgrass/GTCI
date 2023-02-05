package main

import "testing"

func TestFindSumOfThree(t *testing.T) {
	tests := [][]int{{1, -1, -1}, {1, -1, 1}, {1, 2, 4, 6, 8, 20}, {1, 3, 4, 6, 8, 20}}
	targets := []int{2, 2, 31, 31}
	var actualResults []bool
	expectedResults := []bool{false, false, false, true}
	passed := true
	for i, x := range tests {
		result := findSumOfThree(x, targets[i])
		actualResults = append(actualResults, result)
		passed = passed && (result == expectedResults[i])
	}

	if !passed {
		t.Errorf("Expected %v\nResult %v", expectedResults, actualResults)
	}
}

func TestQuickSort(t *testing.T) {

}
