
# 3189. Minimum Moves to Get a Peaceful Board<br> Medium

<p>Given a 2D array <code>rooks</code> of length <code>n</code>, where <code>rooks[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> indicates the position of a rook on an <code>n x n</code> chess board. Your task is to move the rooks <strong>1 cell </strong>at a time vertically or horizontally (to an <em>adjacent</em> cell) such that the board becomes <strong>peaceful</strong>.</p>

<p>A board is <strong>peaceful</strong> if there is <strong>exactly</strong> one rook in each row and each column.</p>

<p>Return the <strong>minimum</strong> number of moves required to get a <em>peaceful board</em>.</p>

<p><strong>Note</strong> that <strong>at no point</strong> can there be two rooks in the same cell.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">rooks = [[0,0],[1,0],[1,1]]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="./assets/image1.gif" style="width: 150px; height: 150px;" /></div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">rooks = [[0,0],[0,1],[0,2],[0,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>
<img alt="" src="./assets/image2.gif" style="width: 200px; height: 200px;" /></div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n == rooks.length &lt;= 500</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= n - 1</code></li>
	<li>The input is generated such that there are no 2 rooks in the same cell.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Greedy`
-	`Sorting`
-	`Counting Sort`

</details>


<details>
<summary> Hint 1 </summary>
Think of a greedy method.
</details>

<details>
<summary> Hint 2 </summary>
First, distribute the rooks in individual rows.
</details>

<details>
<summary> Hint 3 </summary>
You can do this by sorting all rooks by their rows. Then assign the first one to the first row, the second one to the second row, and so on.
</details>

<details>
<summary> Hint 4 </summary>
After you've distributed rooks across all rows, now do the same for columns.
</details>

<details>
<summary> Hint 5 </summary>
Sort rooks by their columns and then assign the first one to the first column and so on.
</details>