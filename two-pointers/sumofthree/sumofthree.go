package main

// insert starter code
func findSumOfThree(nums []int, target int) bool {
	quickSort(nums, greater) // step 1, sort the array
	for idX := 0; idX < len(nums)-2; idX++ {
		x := nums[idX]
		rest := nums[idX+1:]
		highidx := 0
		lowidx := len(rest) - 1
		if x+rest[highidx]+rest[highidx+1] >= target &&
			x+rest[lowidx]+rest[lowidx-1] <= target {
			for lowidx > highidx {
				sum := x + rest[highidx] + rest[lowidx]
				if sum == target {
					return true
				} else if sum > target {
					highidx++
				} else {
					lowidx--
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

func greater(a, b int) bool { return a > b }
