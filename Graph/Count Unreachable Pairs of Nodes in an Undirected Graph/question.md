
# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph<br> Medium

<p>You are given an integer <code>n</code>. There is an <strong>undirected</strong> graph with <code>n</code> nodes, numbered from <code>0</code> to <code>n - 1</code>. You are given a 2D integer array <code>edges</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> denotes that there exists an <strong>undirected</strong> edge connecting nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>.</p>

<p>Return <em>the <strong>number of pairs</strong> of different nodes that are <strong>unreachable</strong> from each other</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="./assets/image1.png" style="width: 267px; height: 169px;" />
<pre>
<strong>Input:</strong> n = 3, edges = [[0,1],[0,2],[1,2]]
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="./assets/image2.png" style="width: 295px; height: 269px;" />
<pre>
<strong>Input:</strong> n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
<strong>Output:</strong> 14
<strong>Explanation:</strong> There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= edges.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no repeated edges.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Depth-First Search`
-	`Breadth-First Search`
-	`Union Find`
-	`Graph`

</details>


<details>
<summary> Hint 1 </summary>
Find the connected components of the graph. To find connected components, you can use Union Find (Disjoint Sets), BFS, or DFS.
</details>

<details>
<summary> Hint 2 </summary>
For a node u, the number of nodes that are unreachable from u is the number of nodes that are not in the same connected component as u.
</details>

<details>
<summary> Hint 3 </summary>
The number of unreachable nodes from node u will be the same for the number of nodes that are unreachable from node v if nodes u and v belong to the same connected component.
</details>