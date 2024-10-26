# Manacher

## m[i] = number of non-empty palindrome centered at i

## Example: 3327. Check if DFS Strings Are Palindromes

``` cpp
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
