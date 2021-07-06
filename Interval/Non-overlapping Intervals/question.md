# 435. Non-overlapping Intervals<br> Medium

## Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

```
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
```

Example 2:

```
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
```

Constraints:

- `1 <= intervals.length <= 2 * 10^4`
- `intervals[i].length == 2`
- `-2 * 104 <= starti < endi <= 2 * 10^4`

<details>

<summary> Related Topics </summary>

-   `Interval`

</details>
