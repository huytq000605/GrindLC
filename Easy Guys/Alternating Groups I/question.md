
# 3206. Alternating Groups I<br> Easy

<p>There is a circle of red and blue tiles. You are given an array of integers <code>colors</code>. The color of tile <code>i</code> is represented by <code>colors[i]</code>:</p>

<ul>
	<li><code>colors[i] == 0</code> means that tile <code>i</code> is <strong>red</strong>.</li>
	<li><code>colors[i] == 1</code> means that tile <code>i</code> is <strong>blue</strong>.</li>
</ul>

<p>Every 3 contiguous tiles in the circle with <strong>alternating</strong> colors (the middle tile has a different color from its <strong>left</strong> and <strong>right</strong> tiles) is called an <strong>alternating</strong> group.</p>

<p>Return the number of <strong>alternating</strong> groups.</p>

<p><strong>Note</strong> that since <code>colors</code> represents a <strong>circle</strong>, the <strong>first</strong> and the <strong>last</strong> tiles are considered to be next to each other.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">colors = [1,1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="./assets/image1.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">colors = [0,1,0,0,1]</span></p>

<p><strong>Output:</strong> 3</p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="./assets/image2.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></p>

<p>Alternating groups:</p>

<p><strong class="example"><img alt="" src="./assets/image3.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></strong><img alt="" src="./assets/image4.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /><strong class="example"><img alt="" src="./assets/image5.png" style="width: 150px; height: 150px; padding: 10px; background: #fff; border-radius: .5rem;" /></strong></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= colors.length &lt;= 100</code></li>
	<li><code>0 &lt;= colors[i] &lt;= 1</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Sliding Window`

</details>


<details>
<summary> Hint 1 </summary>
For each tile, check that the previous and the next tile have different colors from that tile or not.
</details>