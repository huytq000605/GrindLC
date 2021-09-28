# 581. Shortest Unsorted Continuous Subarray<br> Medium

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.

Example 1:

<pre>
Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
</pre>

Example 2:

<pre>
Input: nums = [1,2,3,4]
Output: 0
</pre>

Constraints:

- `1 <= nums.length <= 10^4`
- `-10^5 <= nums[i] <= 10^5`

<details>

<summary> Related Topics </summary>

-   `Stack`
-   `Two Pointers`

</details>
