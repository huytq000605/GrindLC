package main

import "sort"

func removeCoveredIntervals(intervals [][]int) int {
	sort.SliceStable(intervals, func(i, j int) bool {
		if intervals[i][0] < intervals[j][0] {
			return true
		}
		if intervals[i][0] == intervals[j][0] {
			return intervals[i][1] > intervals[j][1]
		} else {
			return false
		}
	})
	result := 1
	max := intervals[0][1]
	for i, interval := range intervals {
		if i == 0 {
			continue
		}
		if interval[0] > max {
			result++
			max = interval[1]
		}
		if interval[1] > max {
			result++
			max = interval[1]
		}

	}
	return result
}
