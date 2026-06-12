# Build Consecutive Values Starting From 0

**Idea:** Sort the coins and sweep from `0`. Track `cur_sum`, the largest value reachable so far (so we can already form every value in `[0, cur_sum]`). A new coin `x` extends the reachable range only if `x <= cur_sum + 1`; otherwise a gap at `cur_sum + 1` can never be filled.

## Related Problems
- #330
- #1798

## Why It Works
If we can already form every value in `[0, cur_sum]`, then adding a coin `x <= cur_sum + 1` lets us form every value in `[0, cur_sum + x]` (each new value `v` is `x` plus some already-reachable `v - x`). Worked examples:

- Coins `[1]` form `0, 1`. To extend, the next coin must be `<= 2`.
- Coins `[1, 2]` form `0, 1, 2, 3`. To extend, the next coin must be `<= 4`.
- Coins `[1, 2, 3]` form `0, 1, 2, 3, 4, 5, 6`. To extend, the next coin must be `<= 7`.

In every case, if the next coin is greater than `cur_sum + 1` (one past the current maximum), there is no way to extend the sequence.

## Algorithm
1. Sort the input and start from `0` with `cur_sum = 0`.
2. For each `arr[i]`:
   - If `arr[i] <= cur_sum + 1`, take it and set `cur_sum = cur_sum + arr[i]`.
   - If `arr[i] > cur_sum + 1`, we cannot extend further.
