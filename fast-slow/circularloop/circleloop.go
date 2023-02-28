package main

func circularArrayLoop(arr []int) bool {
	getCircleIdx := func(currIdx, delta int) int {
		l := len(arr)
		newIdx := (currIdx + delta) % l
		if newIdx < 0 {
			newIdx += l
		}
		return newIdx
	}
	nextIdx := func(idx int) int {
		return getCircleIdx(idx, arr[idx])
	}

	visited := make(map[int]bool)

	for idx := range arr {

		if !visited[idx] {
			circleContinues := func(currIdx int) bool {
				return (arr[idx] > 0) == (arr[currIdx] > 0)
			}

			slow := idx
			fast := idx

			for circleContinues(fast) && circleContinues(nextIdx(fast)) {
				slow = nextIdx(slow)
				visited[fast] = true
				fast = nextIdx(fast)
				visited[fast] = true
				fast = nextIdx(fast)
				if slow == fast {
					return true
				}
			}

		}

	}
	return false
}
