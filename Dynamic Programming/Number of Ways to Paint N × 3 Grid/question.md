# 1411. Number of Ways to Paint N × 3 Grid<br> Hard

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.


Example 1:

<pre>
Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
</pre>

Example 2:

<pre>
Input: n = 5000
Output: 30228214
</pre>

Constraints:

- `n == grid.length`
- `grid[i].length == 3`
- `1 <= n <= 5000`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`
-   `Bit mask`

</details>