# Rolling Hash

## Example: LC 1044: Longest Duplicate Substring

## Pick BASE (pool of each character): 26, 10
## Pick MOD: 2 ^ 31 - 1, ...

## Calculate delete cost for length: deteleCost = (BASE ^ length)
- Must calculate by for loop:
- Steps:
1. deleteCost = 1
2. for n times:
	- delteCost = deleteCost * BASE
	- delteCost %= MOD


## Calculate Hash
### Example with bab => aba
1. First Calculate hash for **bab**
2. Calculate hash for **aba** based on **bab** 

```
banana_val -> [b,a,n,a,n,a] -> [1, 0, 13, 0, 13, 0] (we give every char a number)

ban -> ((1 * 26) * 26) + 13 = 689
ana -> ban + a - b = (689 * 26) + 0 - 26 * 26 * 26 * b = 338 ( the current b had been multiple by 26 three times)
```
### Steps to calculate in real problem
1. Multiply current hash with BASE (keep doing this for ban)
   - hash = hash * BASE
   - hash %= MOD
2. Subtract the first letter
   - hash -= firstLetterCharCode * deleteCost (because first letter * **BASE** for **length** times)
   - hash += MOD (avoid negative number)
   - hash %= MOD
3. Plus with new letter
   - hash += newLetterCharCode

## Prefix Rolling Hash
- We can quickly find rolling hash from [left, right] by precalculate hashs[i] by:
- hashs[i] = ((hashs[i-1] * BASE) + arr[i] - 'a' + 1) % MOD
- powers[i] = (powers[i-1] * BASE) % MOD
- calculate(left, right) = (hashs[right] - hashs[left] * powers[right - left] % MOD + MOD) % MOD
