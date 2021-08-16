package main

func minDifference(nums []int, queries [][]int) []int {
	prefix := make([][]int, len(nums))
	for i := range prefix {
		prefix[i] = make([]int, 100)
	}

	for i := range nums {
		if i == 0 {
			prefix[i][nums[i]-1]++
		} else {
			for j := 0; j < 100; j++ {
				prefix[i][j] = prefix[i-1][j]
			}
			prefix[i][nums[i]-1]++
		}
	}

	cal := func(arr []int) int {
		result := 101
		prev := -1
		for i := 0; i < 100; i++ {
			if arr[i] > 0 {
				if prev != -1 {
					if i-prev < result {
						result = i - prev
					}
				}
				prev = i
			}
		}
		if result == 101 {
			return -1
		}
		return result
	}

	result := make([]int, len(queries))
	arr := make([]int, 100)
	for idx, query := range queries {
		left := query[0]
		right := query[1]
		if left == 0 {
			result[idx] = cal(prefix[right])
		} else {
			for j := 0; j < 100; j++ {
				arr[j] = prefix[right][j] - prefix[left-1][j]
			}
			result[idx] = cal(arr)
		}
	}

	return result
}
