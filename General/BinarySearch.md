# Binary Search (Notes for Myself)

**Idea:** A binary-search signal is when you can bound the answer to a range `[min, max]` and you need to find a value that satisfies some condition over a sorted/monotonic space. You repeatedly probe the midpoint and shrink the range toward the value that fits.

## Handling the Comparison (`<`, `>`, `=`)

When comparing the current value to the condition, the `>` and `<` cases are easy to place; the `=` case is the tricky one.

Example: the question asks for the **minimum index** in an array (sorted ascending) such that `arr[index] < 5`. If `arr[current] >= 5`, you MUST set the next loop bound to `max = current - 1`, because `current` does not fit the condition.

## Choosing the Midpoint Formula (avoiding infinite loops)

As a rule of thumb:

- Use `m = l + (r-l)/2` with `l = m + 1` and `r = m`.
- Use `m = l + (r-l+1)/2` with `l = m` and `r = m - 1`.

This prevents `m` from getting stuck at `r` (or `l`) after the update step.

## Searching for a Minimum That Satisfies a Condition

When the problem asks for the minimum value satisfying a condition: if the current value fits, keep decreasing `max` (or increasing `min`) to narrow down to the real answer.

Example — **Find the Smallest Divisor Given a Threshold**:

- If `sum <= threshold`, you can keep decreasing `max` to look for an even smaller divisor that still fits the condition.
- If `sum > threshold`, the current value is definitely wrong, so set `min = mid + 1`.

The final answer is found when `min == max`.

## Precision Binary Search

When searching over a continuous (floating-point) space, loop until the interval is smaller than a tolerance `eps`:

```cpp
double lo = initial_lo; // Set initial lower bound
double hi = initial_hi; // Set initial upper bound
double eps = 1e-5;      // Tolerance level

while (hi - lo > eps) {
    double mid = (lo + hi) / 2.0;
    if (condition(mid)) {
        lo = mid; // or adjust hi based on your condition
    } else {
        hi = mid;
    }
}
double answer = (lo + hi) / 2.0;
```
