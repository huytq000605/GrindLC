
# 230. Kth Smallest Element in a BST<br> Medium

<p>Given the <code>root</code> of a binary search tree, and an integer <code>k</code>, return <em>the</em> <code>k<sup>th</sup></code> <em>smallest value (<strong>1-indexed</strong>) of all the values of the nodes in the tree</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="./assets/image1.jpg" style="width: 212px; height: 301px;" />
<pre>
<strong>Input:</strong> root = [3,1,4,null,2], k = 1
<strong>Output:</strong> 1
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="./assets/image2.jpg" style="width: 382px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [5,3,6,2,4,null,null,1], k = 3
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is <code>n</code>.</li>
	<li><code>1 &lt;= k &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= Node.val &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?</p>


<details>

<summary> Related Topics </summary>

-	`Tree`
-	`Depth-First Search`
-	`Binary Search Tree`
-	`Binary Tree`

</details>


<details>
<summary> Hint 1 </summary>
Try to utilize the property of a BST.
</details>

<details>
<summary> Hint 2 </summary>
Try in-order traversal. (Credits to @chan13)
</details>

<details>
<summary> Hint 3 </summary>
What if you could modify the BST node's structure?
</details>

<details>
<summary> Hint 4 </summary>
The optimal runtime complexity is O(height of BST).
</details>