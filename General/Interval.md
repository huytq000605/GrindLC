# Interval Patterns

**Idea:** Most greedy interval problems hinge on the right *sort key*. Choosing what to sort by (start vs. end) up front makes the greedy choice obvious.

## Remove All Overlapping Intervals

Sort by **end**, then greedily remove any interval that overlaps the last kept one.

## Only Go to the Right (LeetCode 757 — Set Intersection Size At Least Two)

Sort by end ascending, breaking ties by start descending, so we always extend coverage rightward.

```python
intervals.sort(lambda interval: (interval[1], -interval[0]))
```
