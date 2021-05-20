func singleNonDuplicate(nums []int) int {
	min := 0
	max := len(nums) - 1
	for min < max {
		mid := int(math.Floor(float64(max+min) / 2))
		if mid%2 == 1 {
			mid--
		}
		if nums[mid+1] == nums[mid] {
			min = mid + 2
		} else {
			max = mid
		}
	}
	return nums[min]
}