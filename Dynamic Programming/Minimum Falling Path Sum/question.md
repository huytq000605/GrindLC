# 931. Minimum Falling Path Sum<br> Medium

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:

<pre>
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum underlined below:
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]
</pre>

Example 2:

<pre>
Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is underlined below:
[[-19,57],
 [-40,-5]]
</pre>

Constraints:

- `n == matrix.length`
- `n == matrix[i].length`
- `1 <= n <= 100`
- `-100 <= matrix[i][j] <= 100`

<details>

<summary> Related Topics </summary>

-   `Matrix`
-   `Dynamic Programming`

</details>