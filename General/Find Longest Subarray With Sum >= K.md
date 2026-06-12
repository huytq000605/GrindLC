# Find Longest Subarray with Sum >= K (Prefix Sum + Monotonic Stack)

**Idea:** Build a prefix-sum array so any range sum is `O(1)`, then sweep once while maintaining a **monotonic stack of candidate start positions**. The stack only holds indices whose prefix sum is strictly decreasing, because those are the only positions that can ever be the start of a longest valid subarray.

## How It Works

1. Compute the **prefix sum** array so the sum of any range can be looked up in `O(1)`.
2. Loop through the prefix array, using a **monotonic stack** to save candidate starting positions.
3. A new element is pushed as a valid start only if its prefix value is **strictly smaller** than the top of the stack (or the stack is empty).

## Related Problems

- 962. Maximum Width Ramp
- 862. Shortest Subarray with Sum at Least K
- 1124. Longest Well-Performing Interval
