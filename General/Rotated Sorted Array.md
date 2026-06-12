# Rotated Sorted Array (Binary Search)

**Idea:** Search for a target in a rotated sorted array in `O(log n)` time. For any index we pick as the midpoint, one of the two halves (left or right) is always fully sorted — decide which half is sorted, then check whether the target lies within that sorted half to choose where to search next.

## Complexity

- **Time:** `O(log n)`
- **Space:** `O(1)`
