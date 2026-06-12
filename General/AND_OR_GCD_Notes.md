# AND / OR / GCD Range Queries (Monotonic Accumulation)

**Idea:** As you extend a subarray, the running `AND`, `OR`, or `GCD` is **monotonic** — it can only keep decreasing (`AND`, `GCD`) or increasing (`OR`). Because of this, the set of distinct values produced by all subarrays ending at index `i` stays tiny (at most ~20 for 32-bit numbers), so we can answer range queries for these operators in `O(log n)` distinct values per position.

## Why the value set stays small

Take `&` as an example. For each ending index `i`, keep the set of all distinct results over subarrays that end at `i`:

- `values[i]` = every value produced by starting anywhere and ending at `i`.

Each new element can only turn bits **off**, never back on, so once a bit becomes `0` it stays `0`. With `arr[i] <= 10^9` (under 30 bits), at most ~20–30 distinct values can ever appear, so `len(values[i])` stays small.

## Building the value set

```python
# Take & as an example
# values[i] = every value start from anywhere and ends at i
values[0] = arr[0]
values[1] = [arr[1]] + [arr[1] & value for value in values[0]]
...
values[i + 1] = [arr[i+1]] + [arr[i+1] & value for value in values[i]] 
# len(values[i]) will always be < 20 if arr[i] <= 10^9 (Since the bit cannot change once it was 0)
```

## Notes

- The same monotonic property holds for `OR` (bits only turn on) and `GCD` (values only divide down), so this technique applies to all three operators.
- Deduplicate the values at each step to keep the set bounded; this is what guarantees the `O(log n)` distinct values per position.
