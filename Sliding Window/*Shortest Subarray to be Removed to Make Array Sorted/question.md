# 1574. Shortest Subarray to be Removed to Make Array Sorted<br> Medium

Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

A subarray is a contiguous subsequence of the array.

Return the length of the shortest subarray to remove.

Example 1:

<pre>
Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
</pre>

Example 2:

<pre>
Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
</pre>

Constraints:

- `1 <= arr.length <= 10^5`
- `0 <= arr[i] <= 10^9`

<details>

<summary> Related Topics </summary>

-   `Sliding Window`
-   `Array`

</details>