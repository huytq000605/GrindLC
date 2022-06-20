# 1866. Number of Ways to Rearrange Sticks With K Sticks Visible<br> Hard

There are n uniquely-sized sticks whose lengths are integers from 1 to n. You want to arrange the sticks such that exactly k sticks are visible from the left. A stick is visible from the left if there are no longer sticks to the left of it.

For example, if the sticks are arranged [1,3,2,5,4], then the sticks with lengths 1, 3, and 5 are visible from the left.
Given n and k, return the number of such arrangements. Since the answer may be large, return it modulo 10^9 + 7.

Example 1:

<pre>
Input: n = 3, k = 2
Output: 3
Explanation: [1,3,2], [2,3,1], and [2,1,3] are the only arrangements such that exactly 2 sticks are visible.
The visible sticks are underlined.
</pre>

Example 2:

<pre>
Input: n = 20, k = 11
Output: 647427950
Explanation: There are 647427950 (mod 109 + 7) ways to rearrange the sticks such that exactly 11 sticks are visible.
</pre>

Constraints:

- `1 <= n <= 1000`
- `1 <= k <= n`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`

</details>