
# 1192. Critical Connections in a Network<br> Hard

<p>There are <code>n</code> servers numbered from <code>0</code> to <code>n - 1</code> connected by undirected server-to-server <code>connections</code> forming a network where <code>connections[i] = [a<sub>i</sub>, b<sub>i</sub>]</code> represents a connection between servers <code>a<sub>i</sub></code> and <code>b<sub>i</sub></code>. Any server can reach other servers directly or indirectly through the network.</p>

<p>A <em>critical connection</em> is a connection that, if removed, will make some servers unable to reach some other server.</p>

<p>Return all critical connections in the network in any order.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="./assets/image1.png" style="width: 198px; height: 248px;" />
<pre>
<strong>Input:</strong> n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
<strong>Output:</strong> [[1,3]]
<strong>Explanation:</strong> [[3,1]] is also accepted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, connections = [[0,1]]
<strong>Output:</strong> [[0,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>n - 1 &lt;= connections.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= a<sub>i</sub>, b<sub>i</sub> &lt;= n - 1</code></li>
	<li><code>a<sub>i</sub> != b<sub>i</sub></code></li>
	<li>There are no repeated connections.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Depth-First Search`
-	`Graph`
-	`Biconnected Component`

</details>


<details>
<summary> Hint 1 </summary>
Use Tarjan's algorithm.
</details>