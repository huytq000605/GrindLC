package main

func corpFlightBookings(bookings [][]int, n int) []int {
	result := make([]int, n)
	for _, booking := range bookings {
		result[booking[0]-1] += booking[2]
		if booking[1] < n {
			result[booking[1]] -= booking[2]
		}
	}
	for i := 1; i < n; i++ {
		result[i] += result[i-1]
	}
	return result

}
