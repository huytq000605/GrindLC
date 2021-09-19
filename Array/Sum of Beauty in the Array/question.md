# 2012. Sum of Beauty in the Array<br> Medium

You are given a 0-indexed integer array nums. For each index i (1 <= i <= nums.length - 2) the beauty of nums[i] equals:

- 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
- 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
- 0, if none of the previous conditions holds.
Return the sum of beauty of all nums[i] where 1 <= i <= nums.length - 2.



Example 1:

<pre>
Input: nums = [1,2,3]
Output: 2
Explanation: For each index i in the range 1 <= i <= 1:
- The beauty of nums[1] equals 2.
</pre>

Example 2:

<pre>
Input: nums = [2,4,6,4]
Output: 1
Explanation: For each index i in the range 1 <= i <= 2:
- The beauty of nums[1] equals 1.
- The beauty of nums[2] equals 0.
</pre>

Constraints:

- `3 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

<details>

<summary> Related Topics </summary>

-   `Array`
-	`Prefix`

</details>