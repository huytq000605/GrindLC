
# 3225. Maximum Score From Grid Operations<br> Hard

<p>You are given a 2D matrix <code>grid</code> of size <code>n x n</code>. Initially, all cells of the grid are colored white. In one operation, you can select any cell of indices <code>(i, j)</code>, and color black all the cells of the <code>j<sup>th</sup></code> column starting from the top row down to the <code>i<sup>th</sup></code> row.</p>

<p>The grid score is the sum of all <code>grid[i][j]</code> such that cell <code>(i, j)</code> is white and it has a horizontally adjacent black cell.</p>

<p>Return the <strong>maximum</strong> score that can be achieved after some number of operations.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[0,0,0,0,0],[0,0,3,0,0],[0,1,0,0,0],[5,0,0,3,0],[0,0,0,0,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">11</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="./assets/image1.png" style="width: 300px; height: 200px;" />
<p>In the first operation, we color all cells in column 1 down to row 3, and in the second operation, we color all cells in column 4 down to the last row. The score of the resulting grid is <code>grid[3][0] + grid[1][2] + grid[3][3]</code> which is equal to 11.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[10,9,0,0,15],[7,1,0,8,0],[5,20,0,11,0],[0,0,0,1,2],[8,12,1,10,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">94</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="./assets/image2.png" style="width: 300px; height: 200px;" />
<p>We perform operations on 1, 2, and 3 down to rows 1, 4, and 0, respectively. The score of the resulting grid is <code>grid[0][0] + grid[1][0] + grid[2][1] + grid[4][1] + grid[1][3] + grid[2][3] + grid[3][3] + grid[4][3] + grid[0][4]</code> which is equal to 94.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;=&nbsp;n == grid.length &lt;= 100</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
Use dynamic programming.
</details>

<details>
<summary> Hint 2 </summary>
Solve the problem in O(N^4) using a 3-states dp.
</details>

<details>
<summary> Hint 3 </summary>
Let <code>dp[i][lastHeight][beforeLastHeight]</code> denote the maximum score if the grid was limited to column <code>i</code>, and the height of column <code>i - 1</code> is <code>lastHeight</code> and the height of column <code>i - 2</code> is <code>beforeLastHeight</code>.
</details>

<details>
<summary> Hint 4 </summary>
The third state, <code>beforeLastHeight</code>, is used to determine which values of column <code>i - 1</code> will be added to the score.  We can replace this state with another state that only takes two values 0 or 1.
</details>

<details>
<summary> Hint 5 </summary>
Let <code>dp[i][lastHeight][isBigger]</code> denote the maximum score if the grid was limited to column <code>i</code>, and where the height of column <code>i - 1</code> is <code>lastHeight</code>. Additionally, if <code>isBigger == 1</code>, the number of black cells in column <code>i</code> is assumed to be larger than the number of black cells in column <code>i - 2</code>, and vice versa. Note that if our assumption is wrong, it would lead to a suboptimal score and, therefore, it would not be considered as the final answer.
</details>