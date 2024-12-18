
# 3276. Select Cells in Grid With Maximum Score<br> Hard

<p>You are given a 2D matrix <code>grid</code> consisting of positive integers.</p>

<p>You have to select <em>one or more</em> cells from the matrix such that the following conditions are satisfied:</p>

<ul>
	<li>No two selected cells are in the <strong>same</strong> row of the matrix.</li>
	<li>The values in the set of selected cells are <strong>unique</strong>.</li>
</ul>

<p>Your score will be the <strong>sum</strong> of the values of the selected cells.</p>

<p>Return the <strong>maximum</strong> score you can achieve.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[1,2,3],[4,3,2],[1,1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">8</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="./assets/image1.png" /></p>

<p>We can select the cells with values 1, 3, and 4 that are colored above.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">grid = [[8,7,6],[8,3,2]]</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="./assets/image2.png" style="width: 170px; height: 114px;" /></p>

<p>We can select the cells with values 7 and 8 that are colored above.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= grid.length, grid[i].length &lt;= 10</code></li>
	<li><code>1 &lt;= grid[i][j] &lt;= 100</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Dynamic Programming`
-	`Bit Manipulation`
-	`Matrix`
-	`Bitmask`

</details>


<details>
<summary> Hint 1 </summary>
Sort all the cells in the grid by their values and keep track of their original positions.
</details>

<details>
<summary> Hint 2 </summary>
Try dynamic programming with the following states: the current cell that we might select and a bitmask representing all the rows from which we have already selected a cell so far.
</details>