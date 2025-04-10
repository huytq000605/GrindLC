
# 261. Graph Valid Tree<br> Medium

<p>You have a graph of <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>. You are given an integer n and a list of <code>edges</code> where <code>edges[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> indicates that there is an undirected edge between nodes <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code> in the graph.</p>

<p>Return <code>true</code> <em>if the edges of the given graph make up a valid tree, and</em> <code>false</code> <em>otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="./assets/image1.jpg" style="width: 222px; height: 302px;" />
<pre>
<strong>Input:</strong> n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="./assets/image2.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>Input:</strong> n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>0 &lt;= edges.length &lt;= 5000</code></li>
	<li><code>edges[i].length == 2</code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt; n</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no self-loops or repeated edges.</li>
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
Given <code>n = 5</code> and <code>edges = [[0, 1], [1, 2], [3, 4]]</code>, what should your return? Is this case a valid tree?
</details>

<details>
<summary> Hint 2 </summary>
According to the <a href="https://en.wikipedia.org/wiki/Tree_(graph_theory)" target="_blank">definition of tree on Wikipedia</a>: “a tree is an undirected graph in which any two vertices are connected by <i>exactly</i> one path. In other words, any connected graph without simple cycles is a tree.”
</details>