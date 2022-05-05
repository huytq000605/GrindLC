# 1862. Sum of Floored Pairs<br> Hard

Given an integer array nums, return the sum of floor(nums[i] / nums[j]) for all pairs of indices 0 <= i, j < nums.length in the array. Since the answer may be too large, return it modulo 10^9 + 7.

The floor() function returns the integer part of the division.

Example 1:

<pre>
Input: nums = [2,5,9]
Output: 10
Explanation:
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
We calculate the floor of the division for every pair of indices in the array then sum them up.
</pre>

Example 2:

<pre>
Input: nums = [7,7,7,7,7,7,7]
Output: 49
</pre>

Constraints:

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

<details>

<summary> Related Topics </summary>

-   `Binary Search`
-   `Math`

</details>