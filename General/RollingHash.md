# Rolling Hash

**Idea:** Treat a string as a base-`BASE` number under a modulus `MOD`. Then a sliding window's hash can be updated in O(1) by removing the leftmost character and appending a new one, instead of rehashing the whole window. (Example problem: **LC 1044 — Longest Duplicate Substring**.)

## Setup

- **Pick `BASE`** (the pool size of each character), e.g. `26`, `10`.
- **Pick `MOD`**, e.g. `2^31 - 1`, ...

## Delete Cost for a Window of Length `length`

The delete cost is `deleteCost = BASE ^ length` — the factor by which the leftmost character has been multiplied. It must be computed with a loop (so each multiply can be taken `% MOD`):

1. `deleteCost = 1`
2. Repeat `n` times:
   - `deleteCost = deleteCost * BASE`
   - `deleteCost %= MOD`

## Calculate Hash

Compute the first window's hash, then roll it to the next window. Example with `bab` -> `aba`:

1. First calculate the hash for **bab**.
2. Calculate the hash for **aba** based on **bab**.

```
banana_val -> [b,a,n,a,n,a] -> [1, 0, 13, 0, 13, 0] (we give every char a number)

ban -> ((1 * 26) * 26) + 13 = 689
ana -> ban + a - b = (689 * 26) + 0 - 26 * 26 * 26 * b = 338 ( the current b had been multiple by 26 three times)
```

### Steps to Roll the Hash in a Real Problem

1. Multiply the current hash by `BASE` (do this for each existing char, e.g. `ban`):
   - `hash = hash * BASE`
   - `hash %= MOD`
2. Subtract the first letter:
   - `hash -= firstLetterCharCode * deleteCost` (because the first letter was multiplied by `BASE` for `length` times)
   - `hash += MOD` (avoid a negative number)
   - `hash %= MOD`
3. Add the new letter:
   - `hash += newLetterCharCode`

## Prefix Rolling Hash

Precompute prefix hashes so the hash of any range `[left, right]` can be found quickly:

- `hashs[i] = ((hashs[i-1] * BASE) + arr[i] - 'a' + 1) % MOD`
- `powers[i] = (powers[i-1] * BASE) % MOD`
- `calculate(left, right) = (hashs[right] - hashs[left] * powers[right - left] % MOD + MOD) % MOD`
