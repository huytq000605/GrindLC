package main

func carPooling(trips [][]int, capacity int) bool {
	accumulator := [1001]int
	for _, trip := range trips {
		accumulator[trips[1]] += trips[0]
		accumulator[trips[2]] -= trips[0] 
	}
	currentPeople := 0
	for _, ele := range accumulator {
		currentPeople += ele
		if(currentPeople > capacity) return false
	}
	return true
}
