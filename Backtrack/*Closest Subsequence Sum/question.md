# 1755. Closest Subsequence Sum<br> Hard

You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

Example 1:

<pre>
Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.
</pre>

Example 2:

<pre>
Input: nums = [7,-9,15,-2], goal = -5
Output: 1
Explanation: Choose the subsequence [7,-9,-2], with a sum of -4.
The absolute difference is abs(-4 - (-5)) = abs(1) = 1, which is the minimum.
</pre>

Constraints:

- `1 <= nums.length <= 40`
- `-10^7 <= nums[i] <= 10^7`
- `-10^9 <= goal <= 10^9`

<details>

<summary> Related Topics </summary>

-   `Array`
-   `Backtrack`
-   `Binary Search`

</details>