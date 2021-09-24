# 397. Integer Replacement<br> Medium

Given a positive integer n, you can apply one of the following operations:

- If n is even, replace n with n / 2.
- If n is odd, replace n with either n + 1 or n - 1.

Return the minimum number of operations needed for n to become 1.

Example 1:

<pre>
Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
</pre>

Example 2:

<pre>
Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1
</pre>

Constraints:

- `1 <= n <= 2^31 - 1`

<details>

<summary> Related Topics </summary>

-   `Math`
-   `Dynamic Programming`

</details>