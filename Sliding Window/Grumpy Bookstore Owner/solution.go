package main

func maxSatisfied(customers []int, grumpy []int, minutes int) int {
	maxUnsatisfield := 0           // Create a sliding window that calculate maximum numbers of unsatisfield customers in [minutes] minutes
	for i := 0; i < minutes; i++ { // Create first value for sliding window
		if grumpy[i] == 1 {
			maxUnsatisfield += customers[i]
		}
	}
	start := 0
	currentUnsatisfield := maxUnsatisfield
	for end := minutes; end < len(customers); end++ { // Sliding window
		if grumpy[start] == 1 {
			currentUnsatisfield -= customers[start]
		}
		if grumpy[end] == 1 {
			currentUnsatisfield += customers[end]
		}
		if currentUnsatisfield > maxUnsatisfield {
			maxUnsatisfield = currentUnsatisfield
		}
		start++
	}
	result := 0
	for i := 0; i < len(customers); i++ {
		if grumpy[i] == 0 {
			result += customers[i]
		}
	}
	return result + maxUnsatisfield
}
