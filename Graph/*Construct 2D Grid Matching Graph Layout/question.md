
# 3311. Construct 2D Grid Matching Graph Layout<br> Hard

<p>You are given a 2D integer array <code>edges</code> representing an <strong>undirected</strong> graph having <code>n</code> nodes, where <code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code> denotes an edge between nodes <code>u<sub>i</sub></code> and <code>v<sub>i</sub></code>.</p>

<p>Construct a 2D grid that satisfies these conditions:</p>

<ul>
	<li>The grid contains <strong>all nodes</strong> from <code>0</code> to <code>n - 1</code> in its cells, with each node appearing exactly <strong>once</strong>.</li>
	<li>Two nodes should be in adjacent grid cells (<strong>horizontally</strong> or <strong>vertically</strong>) <strong>if and only if</strong> there is an edge between them in <code>edges</code>.</li>
</ul>

<p>It is guaranteed that <code>edges</code> can form a 2D grid that satisfies the conditions.</p>

<p>Return a 2D integer array satisfying the conditions above. If there are multiple solutions, return <em>any</em> of them.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, edges = [[0,1],[0,2],[1,3],[2,3]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[3,1],[2,0]]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="./assets/image1.png" style="width: 133px; height: 92px;" /></p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 5, edges = [[0,1],[1,3],[2,3],[2,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[4,2,3,1,0]]</span></p>

<p><strong>Explanation:</strong></p>

<p><img src="./assets/image2.png" style="width: 325px; height: 50px;" /></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 9, edges = [[0,1],[0,4],[0,5],[1,7],[2,3],[2,4],[2,5],[3,6],[4,6],[4,7],[6,8],[7,8]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[[8,6,3],[7,4,2],[1,0,5]]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="./assets/image3.png" style="width: 198px; height: 133px;" /></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>1 &lt;= edges.length &lt;= 10<sup>5</sup></code></li>
	<li><code>edges[i] = [u<sub>i</sub>, v<sub>i</sub>]</code></li>
	<li><code>0 &lt;= u<sub>i</sub> &lt; v<sub>i</sub> &lt; n</code></li>
	<li>All the edges are distinct.</li>
	<li>The input is generated such that <code>edges</code> can form a 2D grid that satisfies the conditions.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Hash Table`
-	`Graph`
-	`Matrix`

</details>


<details>
<summary> Hint 1 </summary>
Observe the indegrees of the nodes.
</details>

<details>
<summary> Hint 2 </summary>
The case where there are two nodes with an indegree of 1, and all the others have an indegree of 2 can be handled separately.
</details>

<details>
<summary> Hint 3 </summary>
The nodes with the smallest degrees are the corners.
</details>

<details>
<summary> Hint 4 </summary>
You can simulate the grid creation process using BFS or a similar approach after making some observations on the indegrees.
</details>