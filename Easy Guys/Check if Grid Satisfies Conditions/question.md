
# 3142. Check if Grid Satisfies Conditions<br> Easy

<p>You are given a 2D matrix <code>grid</code> of size <code>m x n</code>. You need to check if each cell <code>grid[i][j]</code> is:</p>

<ul>
	<li>Equal to the cell below it, i.e. <code>grid[i][j] == grid[i + 1][j]</code> (if it exists).</li>
	<li>Different from the cell to its right, i.e. <code>grid[i][j] != grid[i][j + 1]</code> (if it exists).</li>
</ul>

<p>Return <code>true</code> if <strong>all</strong> the cells satisfy these conditions, otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,0,2],[1,0,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="./assets/image1.png" style="width: 254px; height: 186px;padding: 10px; background: #fff; border-radius: .5rem;" /></strong></p>

<p>All the cells in the grid satisfy the conditions.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,1,1],[0,0,0]]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="./assets/image2.png" style="width: 254px; height: 186px;padding: 10px; background: #fff; border-radius: .5rem;" /></strong></p>

<p>All cells in the first row are equal.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1],[2],[3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="./assets/image3.png" style="width: 86px; height: 277px;padding: 10px; background: #fff; border-radius: .5rem;" /></p>

<p>Cells in the first column have different values.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 10</code></li>
	<li><code>0 &lt;= grid[i][j] &lt;= 9</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Matrix`

</details>


<details>
<summary> Hint 1 </summary>
Check if each column has same value in each cell.
</details>

<details>
<summary> Hint 2 </summary>
If the previous condition is satisfied, we can simply check the first cells in adjacent columns.
</details>