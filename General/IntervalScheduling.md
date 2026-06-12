# Interval Scheduling (Single-Interval Scheduling Maximization)

**Idea:** Given `n` intervals, select the largest set of mutually non-overlapping intervals (maximize the number of intervals while minimizing the total length of intervals). The greedy rule **earliest deadline first** is optimal: repeatedly take the interval that finishes earliest, then discard everything it overlaps.

## Why earliest-finish wins

Several intuitive strategies are **not** optimal:

- **Earliest start time** — a very long early interval can block many shorter ones.
- **Shortest interval** or **fewest conflicts** — also not optimal.

The greedy algorithm (from Wikipedia):

1. Select the interval `x` with the **earliest finishing time**.
2. Remove `x` and all intervals intersecting `x` from the candidate set.
3. Repeat until the candidate set is empty.

When we pick an interval in step 1, step 2 may remove many intervals. But all of those necessarily cross the finishing time of `x`, so they all cross each other — meaning **at most one** of them can be in the optimal solution. Hence for every interval in the optimal solution there is a corresponding interval in the greedy solution, which proves the greedy choice is optimal. (A more formal version is given by a charging argument.)

The algorithm runs in `O(n log n)` thanks to the preprocessing step that sorts tasks by finishing time.

## Implementation

```python
# intervals = [(a, b), (c, d), ...]
# Assume each interval start with > 0
intervals.sort(key = lambda: (interval[1], intervals[0]))
prev = -1
result = []
for start, end in intervals:
	if start > prev:
		result.append((start, end))
	prev = end
```
