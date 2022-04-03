# Z-function

## Implementation

``` c++
vector<int> z_function(string s) {
    int n = (int) s.length();
    vector<int> z(n);
		/* 
		We will keep the [l, r] indices of the rightmost segment match.
		That is, among all detected segments we will keep the one that ends rightmost.
		In a way, the index r can be seen as the "boundary" to which our string s has been scanned by the algorithm.
		Everything beyond that point is not yet known.
		*/
    for (int i = 1, l = 0, r = 0; i < n; ++i) {
				/*
					Avoid when we have some cases like:
					s = "aaaabaa"
					when we go to i = 6, we have l = 5, r = 6
					if z[i] = z[i - l] = z[6 - 5] = z[1] = 3 => exceed the string
					=> z[i] = min(r - i + 1, z[i - l])

					Why z[i-l]?
					For this, we observe that the substrings s[l...r] and s[0...r-l] match. 
					This means that as an initial approximation for z[i] we can take the value already computed for the corresponding segment s[0...r-l] 
					and that is z[i-l].
				*/
        if (i <= r)
            z[i] = min (r - i + 1, z[i - l]);
        while (i + z[i] < n && s[z[i]] == s[i + z[i]])
            ++z[i];
        if (i + z[i] - 1 > r)
            l = i, r = i + z[i] - 1;
    }
    return z;
}
```