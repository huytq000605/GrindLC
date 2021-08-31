# 576. Out of Boundary Paths<br> Medium

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 10^9 + 7.

Example 1:

<pre>
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
</pre>

Example 2:

<pre>
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12
</pre>

Constraints:

- `1 <= m, n <= 50`
- `0 <= maxMove <= 50`
- `0 <= startRow < m`
- `0 <= startColumn < n`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`
-   `DFS`

</details>