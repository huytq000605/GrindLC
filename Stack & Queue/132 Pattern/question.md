# 456. 132 Pattern<br> Medium

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:

<pre>
Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
</pre>

Example 2:

<pre>
Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
</pre>

Constraints:

- `n == nums.length`
- `1 <= n <= 2 * 10^5`
- `-10^9 <= nums[i] <= 10^9`

<details>

<summary> Related Topics </summary>

-   `Monotonic Stack`

</details>