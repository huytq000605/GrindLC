# 240. Search a 2D Matrix II<br> Medium

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Example 1:

![](assets/searchgrid2.jpg)

<pre>
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
</pre>

Example 2:

![](assets/searchgrid.jpg)

<pre>
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
</pre>

Constraints:

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= n, m <= 300`
- `-10^9 <= matix[i][j] <= 10^9`
- `All the integers in each row are sorted in ascending order.`
- `All the integers in each column are sorted in ascending order.`
- `-10^9 <= target <= 10^9`

<details>

<summary> Related Topics </summary>

-   `Array`
-   `Matrix`

</details>
