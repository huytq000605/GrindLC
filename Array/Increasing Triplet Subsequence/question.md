# 334. Increasing Triplet Subsequence<br> Medium

## Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

<pre>
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
</pre>

Example 2:

<pre>
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
</pre>

Constraints:

- `1 <= nums.length <= 5 * 10^5`
- `-2^31 <= nums[i] <= 2^31 - 1`

<details>

<summary> Related Topics </summary>

-   `Greedy`
-   `LIS`

</details>