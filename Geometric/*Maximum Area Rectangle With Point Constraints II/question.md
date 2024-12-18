
# 3382. Maximum Area Rectangle With Point Constraints II<br> Hard

<p>There are n points on an infinite plane. You are given two integer arrays <code>xCoord</code> and <code>yCoord</code> where <code>(xCoord[i], yCoord[i])</code> represents the coordinates of the <code>i<sup>th</sup></code> point.</p>

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
<p><strong>Input:</strong> <span class="example-io">xCoord = [1,1,3,3], yCoord = [1,3,1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p><strong class="example"><img alt="Example 1 diagram" src="./assets/image1.png" style="width: 229px; height: 228px;" /></strong></p>

<p>We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border. Hence, the maximum possible area would be 4.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">xCoord = [1,1,3,3,2], yCoord = [1,3,1,3,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>

<p><strong>Explanation:</strong></p>

<p><strong class="example"><img alt="Example 2 diagram" src="./assets/image2.png" style="width: 229px; height: 228px;" /></strong></p>

<p>There is only one rectangle possible is with points <code>[1,1], [1,3], [3,1]</code> and <code>[3,3]</code> but <code>[2,2]</code> will always lie inside it. Hence, returning -1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">xCoord = [1,1,3,3,1,3], yCoord = [1,3,1,3,2,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p><strong class="example"><img alt="Example 3 diagram" src="./assets/image3.png" style="width: 229px; height: 228px;" /></strong></p>

<p>The maximum area rectangle is formed by the points <code>[1,3], [1,2], [3,2], [3,3]</code>, which has an area of 2. Additionally, the points <code>[1,1], [1,2], [3,1], [3,2]</code> also form a valid rectangle with the same area.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= xCoord.length == yCoord.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>0 &lt;= xCoord[i], yCoord[i]&nbsp;&lt;= 8 * 10<sup>7</sup></code></li>
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

</details>


<details>
<summary> Hint 1 </summary>
Process the points by sorting them based on their x-coordinates.
</details>

<details>
<summary> Hint 2 </summary>
For each x-coordinate, sort the corresponding points by y and select two consecutive points y1 and y2 (y1 < y2).
</details>

<details>
<summary> Hint 3 </summary>
Identify the closest x-coordinate (greater than the current x) where some y-coordinates lie in [y1, y2].
</details>

<details>
<summary> Hint 4 </summary>
Use a segment tree to efficiently locate the nearest x-coordinate.
</details>

<details>
<summary> Hint 5 </summary>
Check if the points form a valid rectangle. How?
</details>