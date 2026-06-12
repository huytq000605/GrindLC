# Pascal's Triangle

**Idea:** Repeatedly collapsing an array by adjacent pairwise sums weights each original element by a **binomial coefficient**. After `n-1` rounds on an array of length `n`, the contribution of element `i` is `C(n-1, i)` — exactly the entries of row `n-1` of Pascal's triangle.

## Example: 2221. Find Triangular Sum of an Array

Expanding the pairwise-sum process makes the binomial weights visible:

```
1 2 3 4 5
(1+2) + (2+3) + (3+4) + (4+5)
(1+2+2+3) + (2+3+3+4) + (3+4+4+5)
(1+2+2+2+3+3+3+4) + (2+3+3+3+4+4+4+5)
```

The frequency (weight) of each element across rounds forms Pascal's triangle:

```
freq
1 1 1 1 1
1 2 2 2 1
1 3 4 3 1
1 4 6 4 1
```

So the multiplier for index `i` is `values[i] = C(n-1, i)` for `i` in `range(n)`.

## Notes

- Compute the coefficients lazily using Pascal's recurrence: `nCk = (n-1)C(k-1) + (n-1)Ck`.
