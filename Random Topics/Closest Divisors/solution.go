package main

import "math"

/*
The closest divisors of a number is always near its sqrt
*/

func closestDivisors(num int) []int {
	arr1 := findClosestDivisors(num + 1)
	arr2 := findClosestDivisors(num + 2)
	diff1 := math.Abs(float64(arr1[1] - arr1[0]))
	diff2 := math.Abs(float64(arr2[1] - arr2[0]))
	if diff1 <= diff2 {
		return arr1[:]
	}
	return arr2[:]
}

func findClosestDivisors(num int) [2]int {
	sqrt := int(math.Floor(math.Sqrt(float64(num))))
	for i := sqrt; i >= 1; i-- {
		if num%i == 0 {
			return [2]int{i, num / i}
		}
	}
	return [2]int{0, 0} // never happens
}
