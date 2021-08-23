# 209. Minimum Size Subarray Sum<br> Medium

Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

Example 1:

<pre>
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
</pre>

Example 2:

<pre>
Input: target = 4, nums = [1,4,4]
Output: 1
</pre>

Constraints:

- `1 <= target <= 10^9`
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

<details>

<summary> Related Topics </summary>

-   `Array`
-   `Prefix`

</details>