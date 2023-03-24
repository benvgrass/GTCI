package main

import (
	"math/rand"
	"sort"
	"testing"
)

func TestFindSumOfThree(t *testing.T) {
	tests := [][]int{{1, -1, -1}, {1, -1, 1},
		{1, 2, 4, 6, 8, 20}, {1, 3, 4, 6, 8, 20},
		{3, 7, 1, 2, 8, 4, 5}, {3, 7, 1, 2, 8, 4, 5}, {3, 7, 1, 2, 8, 4, 5},
		{-1, 2, 1, -4, 5, -3}, {-1, 2, 1, -4, 5, -3}, {-1, 2, 1, -4, 5, -3}}
	targets := []int{2, 2, 31, 31, 10, 20, 21, -8, 0, 7}
	var actualResults []bool
	expectedResults := []bool{false, false, false, true, true, true, false, true, true, false}
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
	const x = 10000
	const y = 1000
	const resultRange = 1000
	var a [x][y]int
	for i := 0; i < x; i++ {
		for j := 0; j < y; j++ {
			a[i][j] = rand.Int() % resultRange
		}
	}

	var isSorted [x]bool
	allTrue := true
	notSorted := 0
	for i := 0; i < x; i++ {
		quickSort(a[i][:], greater)
		isSorted[i] = sort.SliceIsSorted(a[i][:],
			func(m, n int) bool { return a[i][m] > a[i][n] })
		allTrue = allTrue && isSorted[i]
		if !isSorted[i] {
			notSorted++
		}
	}

	if !allTrue {
		t.Errorf("%v out of %v arrays were improperly sorted", notSorted, x)
	}

}
