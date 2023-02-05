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

}

func greater(i int, j int) bool { return i > j }

func lazyCheckSort() {
	const x = 5
	const y = 5
	const resultRange = 100
	var a [x][y]int
	for i := 0; i < x; i++ {
		for j := 0; j < y; j++ {
			a[i][j] = rand.Int() % resultRange
		}
	}
	fmt.Printf("%v\n", a)

	var isSorted [x]bool
	allTrue := true
	for i := 0; i < x; i++ {
		quickSort(a[i][:], greater)
		fmt.Printf("a: %v\n", a[i][:])
		var result = sort.SliceIsSorted(a[i][:],
			func(int1, int2 int) bool { return a[i][int1] > a[i][int2] })
		fmt.Printf("%v\n", result)
		isSorted[i] = result
		allTrue = allTrue && isSorted[i]
	}

	fmt.Printf("%v\n%v\n%v", a, isSorted, allTrue)
	fmt.Printf("All sorted? %v", allTrue)
}
