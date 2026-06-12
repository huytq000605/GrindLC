# GCD (Euclidean Algorithm)

**Idea:** The greatest common divisor of `a` and `b` equals the GCD of `b` and `a % b`. Keep replacing the pair `(a, b)` with `(b, a % b)` until `b` becomes `0`; the remaining `a` is the answer.

```typescript
function gcd(a, b) {
    if(a < b) {
        [a, b] = [b, a]
    }
    while(b !== 0) {
        [a, b] = [b, a % b]
    }
    return a
}
```

## Complexity

- **Time:** O(log(min(a, b)))
- **Space:** O(1)

## Notes

- The initial `if (a < b)` swap is optional: one extra loop iteration would swap them anyway via `a % b`. It just avoids that wasted step.
