# 542. 01 Matrix<br> Medium

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.


Example 1:

![](assets/01-1-grid.jpg)

<pre>
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
</pre>

Example 2:

![](assets/01-2-grid.jpg)

<pre>
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
</pre>

Constraints:

- `m == mat.length`
- `n == mat[i].length`
- `1 <= m, n <= 10^4`
- `1 <= m * n <= 10^4`
- `mat[i][j] is either 0 or 1.`
- `There is at least one 0 in mat.`


<details>

<summary> Related Topics </summary>

-   `Breadth-first Search`
-   `Matrix`

</details>