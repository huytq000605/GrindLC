# 1673. Find the Most Competitive Subsequence<br> Medium

Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

Example 1:

<pre>
Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.
</pre>

Example 2:

<pre>
Input: nums = [2,4,3,3,5,4,9,6], k = 4
Output: [2,3,3,4]
</pre>

Constraints:

- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `1 <= k <= nums.length`

<details>

<summary> Related Topics </summary>

-   `Stack`
-   `Monotonic Stack`

</details>
