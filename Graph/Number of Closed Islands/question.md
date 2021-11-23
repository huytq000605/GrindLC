# 1254. Number of Closed Islands<br> Medium

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Example 1:

![](assets/sample_3_1610.png)

<pre>
Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
</pre>

Example 2:

![](assets/sample_4_1610.png)

<pre>
Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
</pre>

Constraints:

- `1 <= grid.length, grid[0].length <= 100`
- `0 <= grid[i][j] <=1`

<details>

<summary> Related Topics </summary>

-   `Graph`
-   `DFS`

</details>