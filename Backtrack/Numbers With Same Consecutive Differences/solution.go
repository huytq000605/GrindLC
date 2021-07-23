package main

func numsSameConsecDiff(n int, k int) []int {
	result := make([]int, 0)
	recursive(n, k, 0, &result)
	return result
}

func recursive(n int, k int, current int, result *[]int) {
	if n == 0 {
		*result = append(*result, current)
		return
	}
	if current > 0 {
		lastNumber := current % 10
		bigger := lastNumber + k
		smaller := lastNumber - k
		if smaller >= 0 && smaller <= 9 {
			recursive(n-1, k, current*10+smaller, result)
		}
		if bigger >= 0 && bigger <= 9 && bigger != smaller {
			recursive(n-1, k, current*10+bigger, result)
		}
	} else {
		for i := 1; i <= 9; i++ {
			recursive(n-1, k, i, result)
		}
	}
}
