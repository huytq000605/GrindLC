# Interval Scheduling (Single-Interval Scheduling Maximization)

- When we n intervals, we want to maximize the number of the intervals and minize the total length of intervals.
- Then we have algorithm (from Wikipedia):
```
Several algorithms, that may look promising at first sight, actually do not find the optimal solution:

Selecting the intervals that start earliest is not an optimal solution, because if the earliest interval happens to be very long, accepting it would make us reject many other shorter requests.
Selecting the shortest intervals or selecting intervals with the fewest conflicts is also not optimal.
The following greedy algorithm, called Earliest deadline first scheduling, does find the optimal solution for unweighted single-interval scheduling:

Select the interval, x, with the earliest finishing time.
Remove x, and all intervals intersecting x, from the set of candidate intervals.
Repeat until the set of candidate intervals is empty.
Whenever we select an interval at step 1, we may have to remove many intervals in step 2. However, all these intervals necessarily cross the finishing time of x, and thus they all cross each other (see figure). Hence, at most 1 of these intervals can be in the optimal solution. Hence, for every interval in the optimal solution, there is an interval in the greedy solution. This proves that the greedy algorithm indeed finds an optimal solution.

A more formal explanation is given by a Charging argument.

The greedy algorithm can be executed in time O(n log n), where n is the number of tasks, using a preprocessing step in which the tasks are sorted by their finishing times.
```

- Can implement it as following:
``` python
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