``` python
is_prime = [1 for i > 1 else 0 for i in range(n+1)]
for num in range(2, n+1):
  if is_prime[num]:
    cur = num * num # We multiply by num because if multiply by a number that < num
                    # We've already computed
    while cur <= n:
      is_prime[cur] = 0
      cur += num
```
