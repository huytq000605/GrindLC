package main

/*
When we calculate s[0]:
if nums[0] = 2 => we've already calculate s[2] and we can sure that set s[2] has less numbers than s[0] ( in this situation is 1 ) ...
*/
func arrayNesting(nums []int) int {
	maxLength := 0
	set := make(map[int]bool)
	for i := 0; i < len(nums); i++ { // Calculate set[i]
		currentLength := 1
		nextNumber := nums[i]             // First number of set
		if _, ok := set[nextNumber]; ok { // If we've already calculated this set => it has less numbers than some sets we had calculated so pass
			continue
		} else {
			set[nextNumber] = true
		}
		for {
			nextNumber = nums[nextNumber]
			if _, ok := set[nextNumber]; ok {
				if currentLength > maxLength {
					maxLength = currentLength
				}
				break
			} else {
				currentLength++
				set[nextNumber] = true
			}
		}
	}
	return maxLength
}
