package main

func maxSatisfied(customers []int, grumpy []int, minutes int) int {
	maxUnsatisfield := 0
	result := 0
	for i := 0; i < minutes; i++ {
		if grumpy[i] == 1 {
			maxUnsatisfield += customers[i]
		} else {
			result += customers[i]
		}
	}
	start := 0
	currentUnsatisfield := maxUnsatisfield
	for end := minutes; end < len(customers); end++ {
		if grumpy[start] == 1 {
			currentUnsatisfield -= customers[start]
		}
		if grumpy[end] == 1 {
			currentUnsatisfield += customers[end]
		} else {
			result += customers[end]
		}
		if currentUnsatisfield > maxUnsatisfield {
			maxUnsatisfield = currentUnsatisfield
		}
		start++
	}
	return result + maxUnsatisfield
}
