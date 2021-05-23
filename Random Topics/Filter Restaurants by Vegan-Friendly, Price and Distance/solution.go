package main

import "sort"

func filterRestaurants(restaurants [][]int, veganFriendly int, maxPrice int, maxDistance int) []int {
	sort.Slice(restaurants, func(i, j int) bool {
		if restaurants[i][1] > restaurants[j][1] {
			return true
		}
		if restaurants[i][1] == restaurants[j][1] {
			if restaurants[i][0] > restaurants[j][0] {
				return true
			} else {
				return false
			}
		} else {
			return false
		}
	})
	result := make([]int, 0)
	for _, res := range restaurants {
		if res[2] >= veganFriendly && res[3] <= maxPrice && res[4] <= maxDistance {
			result = append(result, res[0])
		}
	}
	return result
}
