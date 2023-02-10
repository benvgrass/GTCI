package main

func validPalindrome(s string) bool {
	left := 0
	right := len(s) - 1

	for left <= right {
		if s[left] != s[right] {
			// skip and check
		}
		left++
		right--
	}
	return true
}
