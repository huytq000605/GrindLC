package main

import (
	"sort"
	"strconv"
)

func findMinDifference(timePoints []string) int {
	result := 9999
	sort.Strings(timePoints)
	for i, timePoint := range timePoints {
		if i == len(timePoints)-1 {
			diff := diffMin(timePoints[0], timePoint)
			if diff < result {
				result = diff
			}
		} else {
			diff := diffMin(timePoint, timePoints[i+1])
			if diff < result {
				result = diff
			}
		}
	}
	return result
}

func diffMin(timePoint1 string, timePoint2 string) int {
	hour1, _ := strconv.Atoi(timePoint1[0:2])
	min1, _ := strconv.Atoi(timePoint1[3:])
	hour2, _ := strconv.Atoi(timePoint2[0:2])
	min2, _ := strconv.Atoi(timePoint2[3:])
	diff := (hour2-hour1)*60 + (min2 - min1)
	if diff > 720 {
		diff = 1440 - diff
	}
	return diff
}
