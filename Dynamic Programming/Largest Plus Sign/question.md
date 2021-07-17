# 764. Largest Plus Sign<br> Medium

You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

Example 1:

![](assets/plus1-grid.jpg)

<pre>
Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
</pre>

Example 2:

![](assets/plus2-grid.jpg)

<pre>
Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.
</pre>

Constraints:

- `1 <= n <= 500`
- `1 <= mines.length <= 5000`
- `0 <= xi, yi < n`
- `All the pairs (xi, yi) are unique.`

<details>

<summary> Related Topics </summary>

-   `Array`
-   `Dynamic Programming`

</details>

<details>

<summary> Hint 1 </summary>
For each direction such as "left", find left[r][c] = the number of 1s you will see before a zero starting at r, c and walking left. You can find this in N^2 time with a dp. The largest plus sign at r, c is just the minimum of left[r][c], up[r][c] etc.
</details>