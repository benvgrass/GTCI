package main

import (
	"fmt"
	"math/rand"
	"sort"
)

// insert starter code
func findSumOfThree(nums []int, target int) bool {
	quickSort(nums, greater) // step 1, sort the array
	for idX, x := range nums {
		if x < target {
			for idY, y := range nums[idX+1:] {
				xy := x + y
				if xy < target {
					for idZ := len(nums) - 1; idZ > idX+idY+1 && xy+nums[idZ] <= target; idZ-- {
						if xy+nums[idZ] == target {
							return true
						}
					}
				}
			}
		}
	}
	return false
}

func quickSort(arr []int, less func(i, j int) bool) {
	pivot := 0
	end := len(arr) - 1

	for pivot < end {
		check := pivot + 1
		if less(arr[pivot], arr[check]) {
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
		quickSort(arr[:pivot], less)
	}

	if pivot != len(arr)-1 {
		quickSort(arr[pivot+1:], less)
	}
}

func main() {
	tests := [][]int{{1, -1, -1}, {1, -1, 1}, {1, 2, 4, 6, 8, 20}, {1, 3, 4, 6, 8, 20}}
	targets := []int{2, 2, 31, 31}
	var results []bool
	for i, x := range tests {
		results = append(results, findSumOfThree(x, targets[i]))
	}
	fmt.Printf("%v", results)
}

func greater(i int, j int) bool { return i > j }

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
		quickSort(a[i][:], greater)
		isSorted[i] = sort.SliceIsSorted(a[i][:], greater)
		allTrue = allTrue && isSorted[i]
	}

	// fmt.Printf("%v\n%v\n%v", a, isSorted, allTrue)
	fmt.Printf("All sorted? %v", allTrue)
}
