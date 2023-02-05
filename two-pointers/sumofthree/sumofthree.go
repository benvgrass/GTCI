package main

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

func greater(a, b int) bool { return a > b }
