
# 1245. Tree Diameter<br> Medium

<p>The <strong>diameter</strong> of a tree is <strong>the number of edges</strong> in the longest path in that tree.</p>

<p>There is an undirected tree of <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>. You are given a 2D array <code>edges</code> where <code>edges.length == n - 1</code> and <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an undirected edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the tree.</p>

<p>Return <em>the <strong>diameter</strong> of the tree</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="./assets/image1.jpg" style="width: 224px; height: 145px;" />
<pre>
<strong>Input:</strong> edges = [[0,1],[0,2]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> The longest path of the tree is the path 1 - 0 - 2.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="./assets/image2.jpg" style="width: 224px; height: 225px;" />
<pre>
<strong>Input:</strong> edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> The longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == edges.length + 1</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Tree`
-	`Depth-First Search`
-	`Breadth-First Search`
-	`Graph`
-	`Topological Sort`

</details>


<details>
<summary> Hint 1 </summary>
Start at any node A and traverse the tree to find the furthest node from it, let's call it B.
</details>

<details>
<summary> Hint 2 </summary>
Having found the furthest node B, traverse the tree from B to find the furthest node from it, lets call it C.
</details>

<details>
<summary> Hint 3 </summary>
The distance between B and C is the tree diameter.
</details>