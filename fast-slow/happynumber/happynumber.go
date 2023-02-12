package main

func happyNumber(num int) bool {
	// TODO
	return true
}

func sumOfDigits(num int) int {
	sumDigits := 0
	for n := num; n != 0; n /= 10 {
		d := num % 10
		sumDigits += d * d
	}
	return sumDigits
}
