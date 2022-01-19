# 1027. Longest Arithmetic Subsequence<br> Medium

Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Recall that a subsequence of an array nums is a list nums[i1], nums[i2], ..., nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, and that a sequence seq is arithmetic if seq[i+1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

Example 1:

<pre>
Input: nums = [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
</pre>

Example 2:

<pre>
Input: nums = [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
</pre>

Constraints:

- `2 <= nums.length <= 1000`
- `0 <= nums[i] <= 500`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`
-   `LIS`

</details>