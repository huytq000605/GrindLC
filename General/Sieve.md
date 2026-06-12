# Sieve of Eratosthenes

**Idea:** Mark every number as prime, then for each prime `num`, cross out all of its multiples. We start crossing out from `num * num` because any smaller multiple (`num * k` with `k < num`) was already crossed out when we processed the smaller prime factor `k`.

```python
is_prime = [1 for i > 1 else 0 for i in range(n+1)]
for num in range(2, n+1):
  if is_prime[num]:
    cur = num * num # We multiply by num because if multiply by a number that < num
                    # We've already computed
    while cur <= n:
      is_prime[cur] = 0
      cur += num
```

## Complexity

- **Time:** O(n log log n)
- **Space:** O(n)
