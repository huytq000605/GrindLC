
# 3380. Maximum Area Rectangle With Point Constraints I<br> Medium

<p>You are given an array <code>points</code> where <code>points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> represents the coordinates of a point on an infinite plane.</p>

<p>Your task is to find the <strong>maximum </strong>area of a rectangle that:</p>

<ul>
	<li>Can be formed using <strong>four</strong> of these points as its corners.</li>
	<li>Does <strong>not</strong> contain any other point inside or on its border.</li>
	<li>Has its edges&nbsp;<strong>parallel</strong> to the axes.</li>
</ul>

<p>Return the <strong>maximum area</strong> that you can obtain or -1 if no such rectangle is possible.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[1,1],[1,3],[3,1],[3,3]]</span></p>

<p><strong>Output: </strong>4</p>

<p><strong>Explanation:</strong></p>

<p><strong class="example"><img alt="Example 1 diagram" src="./assets/image1.png" style="width: 229px; height: 228px;" /></strong></p>

<p>We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border<!-- notionvc: f270d0a3-a596-4ed6-9997-2c7416b2b4ee -->. Hence, the maximum possible area would be 4.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[1,1],[1,3],[3,1],[3,3],[2,2]]</span></p>

<p><strong>Output:</strong><b> </b>-1</p>

<p><strong>Explanation:</strong></p>

<p><strong class="example"><img alt="Example 2 diagram" src="./assets/image2.png" style="width: 229px; height: 228px;" /></strong></p>

<p>There is only one rectangle possible is with points <code>[1,1], [1,3], [3,1]</code> and <code>[3,3]</code> but <code>[2,2]</code> will always lie inside it. Hence, returning -1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]</span></p>

<p><strong>Output: </strong>2</p>

<p><strong>Explanation:</strong></p>

<p><strong class="example"><img alt="Example 3 diagram" src="./assets/image3.png" style="width: 229px; height: 228px;" /></strong></p>

<p>The maximum area rectangle is formed by the points <code>[1,3], [1,2], [3,2], [3,3]</code>, which has an area of 2. Additionally, the points <code>[1,1], [1,2], [3,1], [3,2]</code> also form a valid rectangle with the same area.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 10</code></li>
	<li><code>points[i].length == 2</code></li>
	<li><code>0 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 100</code></li>
	<li>All the given points are <strong>unique</strong>.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Math`
-	`Binary Indexed Tree`
-	`Segment Tree`
-	`Geometry`
-	`Sorting`
-	`Enumeration`

</details>


<details>
<summary> Hint 1 </summary>
If <code>(x1, y1)</code> and <code>(x2, y2)</code> are two opposite corners of a rectangle, then the other two would be <code>(x1, y2)</code> and <code>(x2, y1)</code>.
</details>

<details>
<summary> Hint 2 </summary>
Fix two points and find the other two using a set data structure.
</details>

<details>
<summary> Hint 3 </summary>
After determining the rectangle, iterate through the array of points to ensure no point lies on the rectangle’s border or within its interior.
</details>