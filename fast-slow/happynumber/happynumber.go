package main

func happyNumber(num int) bool {
	slow := num
	fast := sumOfDigits(num)

	for fast != 1 {
		if slow == fast {
			return false
		}
		slow = sumOfDigits(slow)
		fast = sumOfDigits(sumOfDigits(fast))
	}
	return true
}

func sumOfDigits(num int) int {
	sumDigits := 0
	for n := num; n != 0; n /= 10 {
		d := n % 10
		sumDigits += d * d
	}
	return sumDigits
}
