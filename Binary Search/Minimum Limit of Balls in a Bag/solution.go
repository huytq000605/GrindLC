package main

func minimumSize(nums []int, maxOperations int) int {
	min := 1
	max := 1000000000
	for min < max {
		mid := min + (max-min)/2
		numOfOperation := 0
		for _, num := range nums {
			numOfOperation += num/mid - 1
			if num%mid != 0 {
				numOfOperation += 1
			}
		}
		if numOfOperation > maxOperations {
			min = mid + 1
		} else {
			max = mid
		}
	}
	return min
}
