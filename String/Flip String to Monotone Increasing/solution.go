package main

// Idea: Choosing the position of first "1" to be the boundary

func minFlipsMonoIncr(s string) int {
	length := len(s)
	prefixOne := make([]int, length)  // number of the "1" till index i
	prefixZero := make([]int, length) // number of the "0" till index i
	totalOne := 0
	totalZero := 0
	result := 0

	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			if i == 0 {
				prefixOne[i] = 1
				prefixZero[i] = 0
			} else {
				prefixOne[i] = prefixOne[i-1] + 1
				prefixZero[i] = prefixZero[i-1]
			}
			totalOne++
		} else {
			if i == 0 {
				prefixOne[i] = 0
				prefixZero[i] = 1
			} else {
				prefixOne[i] = prefixOne[i-1]
				prefixZero[i] = prefixZero[i-1] + 1
			}
			totalZero++
		}
	}

	if totalZero > totalOne { // If we change all the "1" -> "0" or "0" -> "1"
		result = totalOne
	} else {
		result = totalZero
	}

	for firstOnePos := 1; firstOnePos < len(s); firstOnePos++ {
		leftFlip := prefixOne[firstOnePos-1]               // Left flip = number of "1" on the left of firstOnePos
		rightFlip := totalZero - prefixZero[firstOnePos-1] // Right flip = number of "0" on the right of firstOnePos
		totalFlip := leftFlip + rightFlip
		if totalFlip < result {
			result = totalFlip
		}
	}
	return result
}
