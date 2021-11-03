# 368. Largest Divisible Subset<br> Medium

Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.

Example 1:

<pre>
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
</pre>

Example 2:

<pre>
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
</pre>

Constraints:

- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 2 * 10^9`
- `All the integers in nums are unique.`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`

</details>