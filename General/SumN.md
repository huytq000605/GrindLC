# Sum of First N Numbers (Closed-Form Formulas)

**Idea:** Closed-form formulas let you compute these sums in `O(1)` instead of looping.

## Sum of the First N Numbers

$$S = \frac{N(N+1)}{2}$$

```
S = N*(N+1)/2;
```

## Sum of Squares of the First N Numbers

$$S = \frac{N(N+1)(2N+1)}{6}$$

```
S = N*(N+1)*(2N+1)/6;
```

## Complexity

- **Time:** `O(1)`
- **Space:** `O(1)`
