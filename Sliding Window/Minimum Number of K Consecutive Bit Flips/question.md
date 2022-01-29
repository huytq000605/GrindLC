# 995. Minimum Number of K Consecutive Bit Flips<br> Hard

You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.

Example 1:

<pre>
Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
</pre>

Example 2:

<pre>
Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
</pre>

Constraints:

- `1 <= nums.length <= 10^5`
- `1 <= k <= nums.length`

<details>

<summary> Related Topics </summary>

-   `Sliding Window`
-   `Array`
-		`Greedy`

</details>