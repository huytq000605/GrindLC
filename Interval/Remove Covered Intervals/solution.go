package main

func removeCoveredIntervals(intervals [][]int) int {
	sort.SliceStable(intervals, func(i, j int) bool {
			if intervals[i][0] < intervals[j][0] {
					return true
			} else if intervals[i][0] > intervals[j][0] {
					return false
			} else {
					return intervals[i][1] > intervals[j][1]
			}
	})
	cur_end := -1
	result := 0
	for _, interval := range intervals {
			start, end := interval[0], interval[1]
			if start > cur_end || end > cur_end {
					result += 1
			}
			if end > cur_end {
					cur_end = end
			}
	}
	return result
}