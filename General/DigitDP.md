# Digit DP (Digit Dynamic Programming)

**Idea:** The typical problem asks how many numbers satisfying some condition lie in a range `[low, high]`. We cannot simply backtrack over every number because `low` and `high` can be up to `10^18` or even larger. Instead, build a function that counts the valid numbers `<= some value`, processing the value one digit at a time and carrying a small set of states. The answer for `[low, high]` is then `count(high) - count(low - 1)`.

## States: `dp(i, mx, tight, leading_zero)`

- `i` — current digit position, starting from `0`.
- `mx` — the maximum value (the upper bound we are counting under).
- `tight` — whether all previous digits still equal the corresponding digits of `mx`. While `tight` is set, the current digit cannot exceed `mx`'s digit at this position.
- `leading_zero` — whether all previous digits are still `0` (i.e. the number has not "started" yet).
