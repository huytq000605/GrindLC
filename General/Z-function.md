# Z-Function

**Idea:** `z[i] = k` means that starting at index `i`, we can match up to `k` characters of the prefix, i.e. `s[i:i+k-1] == s[0:k]`. We compute every `z[i]` in linear time by reusing a "Z-box" `[l, r]` — the rightmost matched segment found so far — to skip work via the previously computed values.

## How It Works

Maintain `[l, r]`, the interval of the rightmost match seen so far (`s[l:r]` equals a prefix). For each `i`:
- If `i < r`, `i` lies inside the current Z-box, so we can initialize `z[i]` from the mirrored value `z[i - l]`, capped at `r - i` (we cannot rely on matches beyond the box).
- Extend `z[i]` character by character while the prefix keeps matching.
- If the match now reaches past `r`, update the Z-box to `[i, i + z[i]]`.

```python
z = [0 for _ in range(n)]
for i in range(1, n):
    if i < r:
        z[i] = min(r - i, z[i - l])
    while i + z[i] < n and word[i + z[i]] == word[z[i]]:
        z[i] += 1
    if i + z[i] > r:
        l = i
        r = i + z[i]
```

```cpp
vector<int> z_function(string s) {
    int n = s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for(int i = 1; i < n; i++) {
        if(i < r) {
            z[i] = min(r - i, z[i - l]);
        }
        while(i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            z[i]++;
        }
        if(i + z[i] > r) {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}
```

## Complexity

- **Time:** O(n)
- **Space:** O(n) for the `z` array
