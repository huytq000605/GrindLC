
# 2732. Find a Good Subset of the Matrix<br> Hard

<p>You are given a <strong>0-indexed</strong> <code>m x n</code> binary matrix <code>grid</code>.</p>

<p>Let us call a <strong>non-empty</strong> subset of rows <strong>good</strong> if the sum of each column of the subset is at most half of the length of the subset.</p>

<p>More formally, if the length of the chosen subset of rows is <code>k</code>, then the sum of each column should be at most <code>floor(k / 2)</code>.</p>

<p>Return <em>an integer array that contains row indices of a good subset sorted in <strong>ascending</strong> order.</em></p>

<p>If there are multiple good subsets, you can return any of them. If there are no good subsets, return an empty array.</p>

<p>A <strong>subset</strong> of rows of the matrix <code>grid</code> is any matrix that can be obtained by deleting some (possibly none or all) rows from <code>grid</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> We can choose the 0<sup>th</sup> and 1<sup>st</sup> rows to create a good subset of rows.
The length of the chosen subset is 2.
- The sum of the 0<sup>th</sup>&nbsp;column is 0 + 0 = 0, which is at most half of the length of the subset.
- The sum of the 1<sup>st</sup>&nbsp;column is 1 + 0 = 1, which is at most half of the length of the subset.
- The sum of the 2<sup>nd</sup>&nbsp;column is 1 + 0 = 1, which is at most half of the length of the subset.
- The sum of the 3<sup>rd</sup>&nbsp;column is 0 + 1 = 1, which is at most half of the length of the subset.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [[0]]
<strong>Output:</strong> [0]
<strong>Explanation:</strong> We can choose the 0<sup>th</sup> row to create a good subset of rows.
The length of the chosen subset is 1.
- The sum of the 0<sup>th</sup>&nbsp;column is 0, which is at most half of the length of the subset.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> grid = [[1,1,1],[1,1,1]]
<strong>Output:</strong> []
<strong>Explanation:</strong> It is impossible to choose any subset of rows to create a good subset.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= n &lt;= 5</code></li>
	<li><code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
It can be proven, that if there exists a good subset of rows then there exists a good subset of rows with the size of either 1 or 2.
</details>

<details>
<summary> Hint 2 </summary>
To check if there exists a good subset of rows of size 1, we check if there exists a row containing only zeros, if it does, we return its index as a good subset.
</details>

<details>
<summary> Hint 3 </summary>
To check if there exists a good subset of rows of size 2, we iterate over two bit-masks, check if both are presented in the array and if they form a good subset, if they do, return their indices as a good subset.
</details>