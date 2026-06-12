# Longest Increasing Subsequence (LIS)

**Idea:** Maintain a running structure that tracks the best subsequence so far. Two approaches: the **O(n log n)** patience-sorting trick for the classic problem, and a simpler **O(n²)** DP when the problem is a variant.

## Classic: Find the Longest Increasing Subsequence in an Array

Optimal solution in **O(n log n)**:

- Keep a `state` array.
- For each element, if it can replace a `num` inside `state`, replace it (find the position by binary search).
- If it cannot replace any element, append it to `state`.
- The LIS length is `len(state)`.

> Note: `state` is **not** the actual subsequence, only a tool whose length equals the LIS length.

## Variant: Delete Indices Across Many Strings (or Similar)

When the problem is a modification of the classic (e.g. delete indices so that strings form an LIS, or something different), use **Dynamic Programming**.

```python
	n = len(s)
	dp = [1] * n
	for i in range(n):
		for j in range(0, i):
			if s[i] >= s[j]:
				dp[i] = max(dp[i], dp[j] + 1)
	return max(dp)
```

## Complexity

- **Classic (binary search):** Time `O(n log n)`, Space `O(n)`.
- **DP variant:** Time `O(n²)`, Space `O(n)`.
