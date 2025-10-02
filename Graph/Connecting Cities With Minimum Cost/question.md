
# 1135. Connecting Cities With Minimum Cost<br> Medium

<p>There are <code>n</code> cities labeled from <code>1</code> to <code>n</code>. You are given the integer <code>n</code> and an array <code>connections</code> where <code>connections[i] = [x<sub>i</sub>, y<sub>i</sub>, cost<sub>i</sub>]</code> indicates that the cost of connecting city <code>x<sub>i</sub></code> and city <code>y<sub>i</sub></code> (bidirectional connection) is <code>cost<sub>i</sub></code>.</p>

<p>Return <em>the minimum <strong>cost</strong> to connect all the </em><code>n</code><em> cities such that there is at least one path between each pair of cities</em>. If it is impossible to connect all the <code>n</code> cities, return <code>-1</code>,</p>

<p>The <strong>cost</strong> is the sum of the connections&#39; costs used.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="./assets/image1.png" style="width: 161px; height: 141px;" />
<pre>
<strong>Input:</strong> n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
<strong>Output:</strong> 6
<strong>Explanation:</strong> Choosing any 2 edges will connect all cities so we choose the minimum 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="./assets/image2.png" style="width: 136px; height: 91px;" />
<pre>
<strong>Input:</strong> n = 4, connections = [[1,2,3],[3,4,4]]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no way to connect all cities even if all edges are used.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= connections.length &lt;= 10<sup>4</sup></code></li>
	<li><code>connections[i].length == 3</code></li>
	<li><code>1 &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= n</code></li>
	<li><code>x<sub>i</sub> != y<sub>i</sub></code></li>
	<li><code>0 &lt;= cost<sub>i</sub> &lt;= 10<sup>5</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Union Find`
-	`Graph`
-	`Heap (Priority Queue)`
-	`Minimum Spanning Tree`

</details>


<details>
<summary> Hint 1 </summary>
What if we model the cities as a graph?
</details>

<details>
<summary> Hint 2 </summary>
Build a graph of cities and find the minimum spanning tree.
</details>

<details>
<summary> Hint 3 </summary>
You can use a variation of the Kruskal's algorithm for that.
</details>

<details>
<summary> Hint 4 </summary>
Sort the edges by their cost and use a union-find data structure.
</details>

<details>
<summary> Hint 5 </summary>
How to check all cities are connected?
</details>

<details>
<summary> Hint 6 </summary>
At the beginning we have n connected components, each time we connect two components the number of connected components is reduced by one. At the end we should end with only a single component otherwise return -1.
</details>