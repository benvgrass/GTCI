package main

import (
	"fmt"
	"testing"
)

func TestValidPalindrome(t *testing.T) {
	tests := []struct {
		input string
		want  bool
	}{
		{"madame", true},
		{"dead", true},
		{"abca", false},
		{"tebbem", false},
		{"eeccccbebaeeabebccceea", false},
		{"ognfjhgbjhzkqhzadmgqbwqsktzqwjexqvzjsopolnmvnymbbzoofzbbmynvmnloposjzvqxejwqztksqwbqgmdazhqkzhjbghjfno", false},
	}

	for i, tc := range tests {
		t.Run(fmt.Sprintf("ValidPalindromeII.%d", i), func(t *testing.T) {
			res := validPalindrome(tc.input)
			if res != tc.want {
				t.Fatalf("case:%v: actual %v; want %v\n\n", tc.input, res, tc.want)
			} else {
				t.Logf("Pass!")
			}

		})
	}

}
