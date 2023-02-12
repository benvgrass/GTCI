package main

func validPalindrome(s string) bool {
	left := 0
	right := len(s) - 1
	skipped := false

	for left <= right {

		if !skipped && s[left] != s[right] {
			skipped = true
		}
		if skipped && s[left+1] != s[right] && s[left] != s[right-1] {
			return false
		}

		left++
		right--
	}
	return true
}
