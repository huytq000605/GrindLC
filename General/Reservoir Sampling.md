# Reservoir Sampling

**Idea:** A family of randomized algorithms for choosing a simple random sample, **without replacement**, of `k` items from a population of **unknown size** `n` in a single pass over the items. Useful when `n` is unknown, too large to fit in memory, or arrives as a stream.

## Algorithm

1. Put the first `k` elements into the reservoir.
2. For each element starting at index `k+1`, generate a random number `m` in `[0, current n]`.
3. If `m < k`, replace `reservoir[m]` with the current stream element.

This keeps each of the `n` items in the reservoir with equal probability `k/n`.

```python3
fn reservoir(nums, k):
    n = len(nums)
    result = [0 for _ in range(k)]
    for i in range(n):
        r = randint(0, i+1)
        if r < k:
            result[r] = nums[i]
    return result
```

## Complexity

- **Time:** O(n) — single pass over the stream.
- **Space:** O(k) — only the reservoir is stored.
