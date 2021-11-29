# Longest Increasing Subsequence

## Classic: **Just find longest increasing subsequence in an array**

### Optimal Solution: O(nlogn)

### Save a state variable, if element can replace num inside state => replace (Finding place by binary search). If cannot replace any, append to state

### Longest Increasing Subsequence is len(state)

## Modificated: **Delete indexs from many strings to have LIS in string or smt different**

### Use Dynamic Programming
``` python
	n = len(s)
	dp = [1] * n
	for i in range(n):
		for j in range(0, i):
			if s[i] >= s[j]:
				dp[i] = max(dp[i], dp[j] + 1)
	return max(dp)
```
