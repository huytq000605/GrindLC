# KMP

## How to calculate Longest Proper Prefix (LPS) of the Substring
``` python
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

## Using LPS to find pattern in string
``` python
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

## Combined by using O(n+m) space
``` python
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
