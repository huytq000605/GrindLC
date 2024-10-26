# Z-function

# Z function

## Z[i] = k denotes that from i we can match up to k characters from the prefix, which means
## s[i:i+k-1] == s[0:k]

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

``` cpp
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
