
# 3148. Maximum Difference Score in a Grid<br> Medium

<p>You are given an <code>m x n</code> matrix <code>grid</code> consisting of <strong>positive</strong> integers. You can move from a cell in the matrix to <strong>any</strong> other cell that is either to the bottom or to the right (not necessarily adjacent). The score of a move from a cell with the value <code>c1</code> to a cell with the value <code>c2</code> is <code>c2 - c1</code>.<!-- notionvc: 8819ca04-8606-4ecf-815b-fb77bc63b851 --></p>

<p>You can start at <strong>any</strong> cell, and you have to make <strong>at least</strong> one move.</p>

<p>Return the <strong>maximum</strong> total score you can achieve.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="./assets/image1.png" style="width: 240px; height: 240px;" />
<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[9,5,7,3],[8,9,6,1],[6,7,14,3],[2,5,3,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong> We start at the cell <code>(0, 1)</code>, and we perform the following moves:<br />
- Move from the cell <code>(0, 1)</code> to <code>(2, 1)</code> with a score of <code>7 - 5 = 2</code>.<br />
- Move from the cell <code>(2, 1)</code> to <code>(2, 2)</code> with a score of <code>14 - 7 = 7</code>.<br />
The total score is <code>2 + 7 = 9</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="./assets/image2.png" style="width: 180px; height: 116px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[4,3,2],[3,2,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong> We start at the cell <code>(0, 0)</code>, and we perform one move: <code>(0, 0)</code> to <code>(0, 1)</code>. The score is <code>3 - 4 = -1</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>2 &lt;= m, n &lt;= 1000</code></li>
	<li><code>4 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 10<sup>5</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Dynamic Programming`
-	`Matrix`

</details>


<details>
<summary> Hint 1 </summary>
Any path from a cell <code>(x1, y1)</code> to another cell <code>(x2, y2)</code> will always have a score of <code>grid[x2][y2] - grid[x1][y1]</code>.
</details>

<details>
<summary> Hint 2 </summary>
Let’s say we fix the starting cell <code>(x1, y1)</code>, how to the find a cell <code>(x2, y2)</code> such that the value <code>grid[x2][y2] - grid[x1][y1]</code> is the maximum possible?
</details>