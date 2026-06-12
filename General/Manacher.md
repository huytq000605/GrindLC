# Manacher's Algorithm

**Idea:** Compute, for every center `i`, the radius of the longest palindrome centered there in linear time. The key trick is reusing already-computed radii: when `i` lies inside the current rightmost palindrome `[l, r]`, its mirror `l + (r - i)` gives a free lower bound on `m[i]`, so we only ever expand past what we've already proven.

Here `m[i]` is the number of non-empty palindromes centered at `i` (equivalently, the palindrome radius at `i`).

This version handles **odd-length** palindromes only. To also cover even-length palindromes, run it on the string with separator characters inserted between every position.

## Example: 3327. Check if DFS Strings Are Palindromes

```cpp
vector<int> manacher_odd(const string &s) {
    int n = s.size();
    vector<int> m(n, 0);
    int l = 0, r = 0;
    for(int i = 1; i < n; ++i) {
        if(i < r) {
            m[i] = min(r-i, m[l+(r-i)]);
        }
        while(i - m[i] >= 0 && i + m[i] < n && s[i - m[i]] == s[i + m[i]]) {
            ++m[i];
        }
        if(i + m[i] > r) {
            r = i + m[i];
            l = i - m[i];
        }
    }
    return m;
}
```

## Complexity

- **Time:** `O(n)` — each position is expanded past at most once amortized.
- **Space:** `O(n)` for the radius array `m`.
