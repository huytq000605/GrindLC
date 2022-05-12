package main

func combinationSum3(k int, n int) [][]int {
	result := make([][]int, 0)
	cur := make([]int, 0)
	var dfs func(int, int)
	dfs = func(num int, total int) {
		if len(cur) == k && total == n {
			toResult := make([]int, len(cur))
			copy(toResult, cur)
			result = append(result, toResult)
		}
		if len(cur) >= k || total >= n || num > 9 {
			return
		}
		cur = append(cur, num)
		dfs(num+1, total+num)
		cur = cur[:len(cur)-1]
		dfs(num+1, total)
	}
	dfs(1, 0)
	return result
}
