package main

import "fmt"

func maximalNetworkRank(n int, roads [][]int) int {
	if len(roads) == 0 {
		return 0
	}
	if len(roads) == 1 {
		return 1
	}
	numOfConnected := make(map[int]int) // Num of connected city of each city
	connection := make(map[string]bool) // Save connection to lookup
	for _, road := range roads {
		numOfConnected[road[0]]++
		numOfConnected[road[1]]++
		key1 := fmt.Sprintf("%v-%v", road[0], road[1])
		key2 := fmt.Sprintf("%v-%v", road[1], road[0])
		connection[key1] = true
		connection[key2] = true
	}

	// Finding 2 biggest num of connected
	firstMax := 0
	secondMax := 0
	for _, num := range numOfConnected {
		if num > firstMax && num > secondMax {
			secondMax = firstMax
			firstMax = num
		} else if num > secondMax && num <= firstMax {
			secondMax = num
		}
	}

	// Get all the cities have num of connected = the biggest num of connected
	firstMaxCities := []int{}
	for city, num := range numOfConnected {
		if num == firstMax {
			firstMaxCities = append(firstMaxCities, city)
		}
	}

	// Check if the first and second biggest num of connected doesn't have connection then just return total connected
	for _, firstMaxCity := range firstMaxCities {
		for city, num := range numOfConnected {
			if num == secondMax && city != firstMaxCity {
				key := fmt.Sprintf("%v-%v", city, firstMaxCity)
				if _, ok := connection[key]; !ok {
					return firstMax + secondMax
				}
			}
		}
	}

	return firstMax + secondMax - 1
}
