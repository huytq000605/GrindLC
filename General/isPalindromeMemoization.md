# Palindrome Check with Memoization

**Idea:** Check whether the substring `s[left..right]` is a palindrome by comparing the two ends and recursing inward. `@lru_cache` memoizes each `(left, right)` pair so overlapping subproblems are computed only once — useful when many palindrome checks are needed (e.g. palindrome-partitioning DP).

```python
 @lru_cache(None)
        def isPalindrome(left, right):
            if left >= right:
                return True
            if s[left] != s[right]:
                return False
            return isPalindrome(left + 1, right - 1)
```

## Complexity

- **Time:** O(n^2) overall to fill the cache (O(n^2) distinct `(left, right)` pairs, each O(1) with memoization).
- **Space:** O(n^2) for the memoization cache, plus O(n) recursion stack.
