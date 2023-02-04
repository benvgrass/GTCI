package main

import (
	"fmt"
	"math/rand"
	"sort"
)

// insert starter code
func findSumOfThree(nums []int, target int) bool {
	quickSort(nums) // step 1
	return true
}

func quickSort(arr []int) {
	pivot := 0
	end := len(arr) - 1

	for pivot < end {
		check := pivot + 1
		if arr[pivot] < arr[check] {
			if check != end {
				arr[check], arr[end] = arr[end], arr[check]
			}
			end--
		} else {
			arr[pivot], arr[check] = arr[check], arr[pivot]
			pivot++
		}
	}

	if pivot != 0 {
		quickSort(arr[:pivot])
	}

	if pivot != len(arr)-1 {
		quickSort(arr[pivot+1:])
	}
}

func main() {
	lazyCheckSort() // lazily check whether quicksort implementation works
}

func lazyCheckSort() {
	const x = 10000
	const y = 1000
	const resultRange = 1000
	var a [x][y]int
	for i := 0; i < x; i++ {
		for j := 0; j < y; j++ {
			a[i][j] = rand.Int() % resultRange
		}
	}
	// fmt.Printf("%v\n", a)

	var isSorted [x]bool
	allTrue := true
	for i := 0; i < x; i++ {
		quickSort(a[i][:])
		isSorted[i] = sort.SliceIsSorted(a[i][:], func(i int, j int) bool { return i < j })
		allTrue = allTrue && isSorted[i]
	}

	// fmt.Printf("%v\n%v\n%v", a, isSorted, allTrue)
	fmt.Printf("All sorted? %v", allTrue)
}
