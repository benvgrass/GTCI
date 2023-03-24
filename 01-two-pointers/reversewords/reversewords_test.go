package main

import (
	"testing"
)

func TestReverseWordsLazy(t *testing.T) {
	tests := []string{"We love Go", "To be or not to be",
		"You are amazing", "Hello     World", "Hey"}
	expected := []string{"Go love We", "be to not or be To",
		"amazing are You", "World Hello", "Hey"}
	results := make([]string, len(tests))
	pass := true

	for i, t := range tests {
		results[i] = reverseWordsLazy(t)
		pass = pass && results[i] == expected[i]
	}

	if !pass {
		t.Errorf("Expected %v\nResult %v", expected, results)
	}
}
