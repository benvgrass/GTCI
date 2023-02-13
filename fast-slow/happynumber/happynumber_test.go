package main

import (
	"fmt"
	"testing"
)

func TestHappyNumber(t *testing.T) {
	tests := []struct {
		input    int
		expected bool
	}{
		{2147483646, false},
		{19, false},
		{1, true},
		{8, false},
		{7, true},
		{2, false},
		{145, false},
		{2211, true},
	}

	for i, tc := range tests {
		t.Run(fmt.Sprintf("HappyNumber.%d", i), func(t *testing.T) {
			res := happyNumber(tc.input)
			if res != tc.expected {
				t.Fatalf("input:%v: expected %v; want %v", tc.input, res, tc.expected)
			} else {
				t.Logf("Pass!")
			}

		})
	}
}

func TestSumOfDigits(t *testing.T) {
	tests := []struct {
		input    int
		expected int
	}{
		{1, 1},
		{19, 82},
		{27, 53},
		{11, 2},
		{2147483646, 247},
		{97, 130},
		{13, 10},
		{10, 1},
		{89, 145},
		{42, 20},
		{69, 117},
	}

	for i, tc := range tests {
		t.Run(fmt.Sprintf("SumOfDigits.%d", i), func(t *testing.T) {
			res := sumOfDigits(tc.input)
			if res != tc.expected {
				t.Fatalf("input:%v: expected %v; want %v", tc.input, res, tc.expected)
			} else {
				t.Logf("Pass!")
			}

		})
	}
}
