# 1420. Build Array Where You Can Find The Maximum Exactly K Comparisons<br> Hard

Given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:

![](assets/e.png)

You should build the array arr which has the following properties:

- arr has exactly n integers.
- 1 <= arr[i] <= m where (0 <= i < n).
- After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:

<pre>
Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
</pre>

Example 2:

<pre>
Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
</pre>

Constraints:

- `1 <= n <= 50`
- `1 <= m <= 100`
- `0 <= k <= n`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`

</details>