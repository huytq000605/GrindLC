package main

func carPooling(trips [][]int, capacity int) bool {
	currentPeople := []int{}
	for _, trip := range trips {
		for i := trip[1]; i < trip[2]; i++ {
			for i >= len(currentPeople) {
				currentPeople = append(currentPeople, 0)
			}
			currentPeople[i] = currentPeople[i] + trip[0]

		}
	}
	for _, ele := range currentPeople {
		if ele > capacity {
			return false
		}
	}
	return true
}
