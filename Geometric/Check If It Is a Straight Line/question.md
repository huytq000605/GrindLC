
# 1232. Check If It Is a Straight Line<br> Easy

<p>You are given an array&nbsp;<code>coordinates</code>, <code>coordinates[i] = [x, y]</code>, where <code>[x, y]</code> represents the coordinate of a point. Check if these points&nbsp;make a straight line in the XY plane.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="./assets/image1.jpg" style="width: 336px; height: 336px;" /></p>

<pre>
<strong>Input:</strong> coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="./assets/image2.jpg" style="width: 348px; height: 336px;" /></strong></p>

<pre>
<strong>Input:</strong> coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;=&nbsp;coordinates.length &lt;= 1000</code></li>
	<li><code>coordinates[i].length == 2</code></li>
	<li><code>-10^4 &lt;=&nbsp;coordinates[i][0],&nbsp;coordinates[i][1] &lt;= 10^4</code></li>
	<li><code>coordinates</code>&nbsp;contains no duplicate point.</li>
</ul>

<details>

<summary> Related Topics </summary>

-	`Array`
-	`Math`
-	`Geometry`

</details>


<details>
<summary> Hint 1 </summary>
If there're only 2 points, return true.
</details>

<details>
<summary> Hint 2 </summary>
Check if all other points lie on the line defined by the first 2 points.
</details>

<details>
<summary> Hint 3 </summary>
Use cross product to check collinearity.
</details>