# KMP (Knuth-Morris-Pratt String Matching)

## Idea

Whenever we hit a mismatch, we check whether the current matched suffix is also a prefix of the pattern. If so, we fall back to that previous prefix and keep retrying — repeating until we either get a match or run out of suffix to fall back to. This lets us avoid re-scanning characters we've already matched.

## Build the LPS (Longest Prefix-Suffix) table

`lps[i]` is the length of the longest proper prefix of `s[0..i]` that is also a suffix of `s[0..i]`.

```python
def lps(s):
    n = len(s)
    j = 0
    lps = [0 for _ in range(n)]
    for i in range(1, n):
        while j and s[i] != s[j]:
            j = lps[j-1]
        if s[i] == s[j]:
            j += 1
            lps[i] = j
    return lps
```

## Use LPS to find a pattern in a string

Returns the start indices of every occurrence of pattern `p` in string `s`.

```python
def find_matches(s, p):
    matched = []
    pattern_lps = lps(p)
    j = 0
    for i in range(len(s)):
        while j and s[i] != p[j]:
            j = pattern_lps[j-1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                matched.append(i- len(p) + 1)
                j = pattern_lps[j]
            else:
                j += 1
    return matched
```

## Combined variant using O(n + m) space

Concatenate `p + "#" + s` (with a separator character that appears in neither string), build one LPS table over the whole thing, and report positions where the LPS reaches the full pattern length.

```python
def find_matches(s, p):
    s = p + "#" + s
    n = len(s)
    lps = [0 for _ in range(n)]
    j = 0
    for i in range(1, n):
        while j and s[i] != s[j]:
            j = lps[j-1]
        if s[i] == s[j]:
            j += 1
        lps[i] = j
    return [i-len(p)-len(p) for i in range(len(p)+1, n) if lps[i] >= len(p)]
```

## Complexity

- **Time:** O(n + m) — building the LPS table for the pattern is O(m), and scanning the text is O(n).
- **Space:** O(m) for the standalone LPS table; O(n + m) for the combined variant (it builds the table over `p + "#" + s`).
