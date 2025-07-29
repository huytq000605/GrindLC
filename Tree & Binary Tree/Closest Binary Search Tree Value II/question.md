
# 272. Closest Binary Search Tree Value II<br> Hard

<p>Given the <code>root</code> of a binary search tree, a <code>target</code> value, and an integer <code>k</code>, return <em>the </em><code>k</code><em> values in the BST that are closest to the</em> <code>target</code>. You may return the answer in <strong>any order</strong>.</p>

<p>You are <strong>guaranteed</strong> to have only one unique set of <code>k</code> values in the BST that are closest to the <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="./assets/image1.jpg" style="width: 292px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [4,2,5,1,3], target = 3.714286, k = 2
<strong>Output:</strong> [4,3]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1], target = 0.000000, k = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>9</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= target &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Assume that the BST is balanced. Could you solve it in less than <code>O(n)</code> runtime (where <code>n = total nodes</code>)?</p>


<details>

<summary> Related Topics </summary>

-	`Two Pointers`
-	`Stack`
-	`Tree`
-	`Depth-First Search`
-	`Binary Search Tree`
-	`Heap (Priority Queue)`
-	`Binary Tree`

</details>


<details>
<summary> Hint 1 </summary>
Consider implement these two helper functions:
<ol type="i"><li><code>getPredecessor(N)</code>, which returns the next smaller node to N.</li>
<li><code>getSuccessor(N)</code>, which returns the next larger node to N.</li>
</ol>
</details>

<details>
<summary> Hint 2 </summary>
Try to assume that each node has a parent pointer, it makes the problem much easier.
</details>

<details>
<summary> Hint 3 </summary>
Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
</details>

<details>
<summary> Hint 4 </summary>
You would need two stacks to track the path in finding predecessor and successor node separately.
</details>