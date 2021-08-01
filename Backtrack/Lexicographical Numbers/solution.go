package main

func lexicalOrder(n int) []int {
	result := make([]int, 0)
	if n < 10 {
		for i := 1; i <= n; i++ {
			dfs(i, n, &result)
		}
	} else {
		for i := 1; i < 10; i++ {
			dfs(i, n, &result)
		}
	}
	return result
}

func dfs(num int, n int, result *[]int) {
	*result = append(*result, num)
	for i := 0; i < 10; i++ {
		if num*10+i <= n {
			dfs(num*10+i, n, result)
		} else {
			return
		}
	}
}
