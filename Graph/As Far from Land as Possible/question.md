# 1162. As Far from Land as Possible<br> Medium

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.


Example 1:

![](assets/1336_ex1.jpeg)

<pre>
Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
</pre>

Example 2:

![](assets/1336_ex2.jpeg)

<pre>
Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
</pre>

Constraints:

- `n == grid.length`
- `n == grid[i].length`
- `1 <= n <= 100`
- `grid[i][j] is 0 or 1`

<details>

<summary> Related Topics </summary>

-   `Breadth-first Search`
-   `Matrix`

</details>

<details>

<summary> Hint 1 </summary>
Can you think of this problem in a backwards way ?
</details>
<details>

<summary> Hint 2 </summary>
Imagine expanding outward from each land cell. What kind of search does that ?
</details>

<details>
<summary> Hint 3 </summary>
Use BFS starting from all land cells in the same time.
</details>

<details>

<summary> Hint 4 </summary>
When do you reach the furthest water cell?
</details>
