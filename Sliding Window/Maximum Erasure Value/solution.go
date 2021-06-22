package main

func maximumUniqueSubarray(nums []int) int {
	start := 0
	result := 0
	seen := make(map[int]int)
	prefixSum := make([]int, len(nums))
	for i, num := range nums {
		if seenNumIdx, ok := seen[num]; ok {
			if seenNumIdx >= start {
				start = seenNumIdx + 1
			}
		}
		seen[num] = i
		if i == 0 {
			prefixSum[i] = num
		} else {
			prefixSum[i] = prefixSum[i-1] + num
		}

		score := 0
		if start == 0 {
			score = prefixSum[i]
		} else {
			score = prefixSum[i] - prefixSum[start-1]
		}

		if score > result {
			result = score
		}
	}
	return result
}
