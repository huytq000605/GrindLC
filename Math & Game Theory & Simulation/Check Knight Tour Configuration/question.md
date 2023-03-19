
# 2596. Check Knight Tour Configuration<br> Medium

<p>There is a knight on an <code>n x n</code> chessboard. In a valid configuration, the knight starts <strong>at the top-left cell</strong> of the board and visits every cell on the board <strong>exactly once</strong>.</p>

<p>You are given an <code>n x n</code> integer matrix <code>grid</code> consisting of distinct integers from the range <code>[0, n * n - 1]</code> where <code>grid[row][col]</code> indicates that the cell <code>(row, col)</code> is the <code>grid[row][col]<sup>th</sup></code> cell that the knight visited. The moves are <strong>0-indexed</strong>.</p>

<p>Return <code>true</code> <em>if</em> <code>grid</code> <em>represents a valid configuration of the knight&#39;s movements or</em> <code>false</code> <em>otherwise</em>.</p>

<p><strong>Note</strong> that a valid knight move consists of moving two squares vertically and one square horizontally, or two squares horizontally and one square vertically. The figure below illustrates all the possible eight moves of a knight from some cell.</p>
<img alt="" src="./assets/image1.png" style="width: 300px; height: 300px;" />
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="./assets/image2.png" style="width: 251px; height: 251px;" />
<pre>
<strong>Input:</strong> grid = [[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]]
<strong>Output:</strong> true
<strong>Explanation:</strong> The above diagram represents the grid. It can be shown that it is a valid configuration.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="./assets/image3.png" style="width: 151px; height: 151px;" />
<pre>
<strong>Input:</strong> grid = [[0,3,6],[5,8,1],[2,7,4]]
<strong>Output:</strong> false
<strong>Explanation:</strong> The above diagram represents the grid. The 8<sup>th</sup> move of the knight is not valid considering its position after the 7<sup>th</sup> move.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == grid.length == grid[i].length</code></li>
	<li><code>3 &lt;= n &lt;= 7</code></li>
	<li><code>0 &lt;= grid[row][col] &lt; n * n</code></li>
	<li>All integers in <code>grid</code> are <strong>unique</strong>.</li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
It is enough to check if each move of the knight is valid.
</details>

<details>
<summary> Hint 2 </summary>
Try all cases of the knight's movements to check if a move is valid.
</details>