package two_pointers

import (
	"fmt"
	"strings"
)

func isPalindrome(inputString string) bool {
	left := 0
	right := len(inputString) - 1

	for left <= right {
		if inputString[left] != inputString[right] {
			return false
		}
		left++
		right--
	}
	return true
}

// driver code from educative.io course to test isPalindrome function
func main() {
	str := []string{"RACEACAR", "A", "ABCDEFGFEDCBA", "ABC", "ABCBA", "ABBA", "RACEACAR"}
	for i, s := range str {
		fmt.Printf("Test Case # %d\n", i+1)
		fmt.Printf("%s\n", strings.Repeat("-", 100))
		fmt.Printf("\tThe input string is '%s' and the length of the string is %d.\n", s, len(s))
		fmt.Printf("\n\tIs it a palindrome?.....%v\n", isPalindrome(s))
		fmt.Printf("%s\n", strings.Repeat("-", 100))
	}
}
