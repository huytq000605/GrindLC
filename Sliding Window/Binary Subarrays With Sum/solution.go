/*
I track all the "1" make the sum change, if goal == 0 then we have some situation that makes idxOne have zero ele
If sum > 0, keep tracking all 1 like every other sliding window problem
When "sum" == "goal", i increase "result" by how many sub array i can made at that "end"
*/

package main

func numSubarraysWithSum(nums []int, goal int) int {
	sum := 0
	start := 0
	result := 0
	idxOne := make([]int, 0)
	for end := range nums {
		if nums[end] == 1 {
			sum++
			idxOne = append(idxOne, end)
			if sum > goal {
				sum--
				start = idxOne[0] + 1
				idxOne = idxOne[1:]
			}
		}
		if sum == goal {
			if len(idxOne) == 0 { // case goal == 0
				result++
				result += end - start + 1
			} else {
				result++
				result += idxOne[0] - start + 1
			}

		}
	}
	return result
}
