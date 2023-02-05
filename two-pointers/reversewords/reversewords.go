package main

import (
	"strings"
)

func reverseWordsLazy(sentence string) string {
	// write your code here
	// your code will replace this placeholder return statement
	lst := strings.Fields(sentence)
	low, high := 0, len(lst)-1
	for low < high {
		lst[low], lst[high] = lst[high], lst[low]
		low++
		high--
	}
	return strings.Join(lst, " ")
}
