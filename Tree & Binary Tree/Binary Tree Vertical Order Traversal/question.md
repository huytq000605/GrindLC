
# 314. Binary Tree Vertical Order Traversal<br> Medium

<p>Given the <code>root</code> of a binary tree, return <em><strong>the vertical order traversal</strong> of its nodes&#39; values</em>. (i.e., from top to bottom, column by column).</p>

<p>If two nodes are in the same row and column, the order should be from <strong>left to right</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="./assets/image1.jpg" style="width: 282px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [3,9,20,null,null,15,7]
<strong>Output:</strong> [[9],[3,15],[20],[7]]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="./assets/image2.jpg" style="width: 462px; height: 222px;" />
<pre>
<strong>Input:</strong> root = [3,9,8,4,0,1,7]
<strong>Output:</strong> [[4],[9],[3,0,1],[8],[7]]
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="./assets/image3.jpg" style="width: 462px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [3,9,8,4,0,1,7,null,null,null,2,5]
<strong>Output:</strong> [[4],[9,5],[3,0,1],[8,2],[7]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Hash Table`
-	`Tree`
-	`Depth-First Search`
-	`Breadth-First Search`
-	`Sorting`
-	`Binary Tree`

</details>


<details>
<summary> Hint 1 </summary>
Do BFS from the root. Let the root be at column 0. In the BFS, keep in the queue the node and its column.
</details>

<details>
<summary> Hint 2 </summary>
When you traverse a node, store its value in the column index. For example, the root's value should be stored at index 0.
</details>

<details>
<summary> Hint 3 </summary>
If the node has a left node, it column should be col - 1. Similarly, if the node has a right node, its column should be col + 1.
</details>

<details>
<summary> Hint 4 </summary>
At the end, check the minimum and maximum col and output their values.
</details>