# 1785. Minimum Elements to Add to Form a Given Sum<br> Medium

You are given an integer array nums and two integers limit and goal. The array nums has an interesting property that abs(nums[i]) <= limit.

Return the minimum number of elements you need to add to make the sum of the array equal to goal. The array must maintain its property that abs(nums[i]) <= limit.

Note that abs(x) equals x if x >= 0, and -x otherwise.

Example 1:

<pre>
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
</pre>

Constraints:

- `0 <= c <= 2^31 - 1`

<details>

<summary> Related Topics </summary>

-   `Two Pointers`
-   `Math`

</details>