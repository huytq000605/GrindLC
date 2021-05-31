package main

func maxChunksToSorted(arr []int) int {
	// for easy to understand, i use sliding window and store start & end number
	startNumber := 0
	endNumber := -1
	startIndex := 0
	chunks := 0
	for endIndex := 0; endIndex < len(arr); endIndex++ {
		if arr[endIndex] > endNumber {
			endNumber = arr[endIndex]
		}
		if (endIndex - startIndex + 1) == (endNumber - startNumber + 1) {
			chunks++
			startNumber = endNumber + 1
			startIndex = endIndex + 1
			endNumber = -1
		}
	}
	return chunks
}
