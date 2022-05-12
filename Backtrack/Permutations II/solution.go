package main

func permuteUnique(nums []int) [][]int {
	cur := make([]int, 0)
	result := make([][]int, 0)
	n := len(nums)
	var dfs func(i int)
	dfs = func(i int) {
		if len(cur) == n {
			toResult := make([]int, n)
			copy(toResult, cur)
			result = append(result, toResult)
		}
		if i >= n {
			return
		}
		seen := make(map[int]struct{})
		for j := i; j < n; j++ {
			if _, ok := seen[nums[j]]; !ok {
				seen[nums[j]] = struct{}{}
				cur = append(cur, nums[j])
				nums[i], nums[j] = nums[j], nums[i]
				dfs(i + 1)
				cur = cur[:len(cur)-1]
				nums[i], nums[j] = nums[j], nums[i]
			}
		}
	}
	dfs(0)
	return result
}
