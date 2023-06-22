
# 1214. Two Sum BSTs<br> Medium

<p>Given the roots of two binary search trees, <code>root1</code> and <code>root2</code>, return <code>true</code> if and only if there is a node in the first tree and a node in the second tree whose values sum up to a given integer <code>target</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="./assets/image1.png" style="width: 369px; height: 169px;" />
<pre>
<strong>Input:</strong> root1 = [2,1,4], root2 = [1,0,3], target = 5
<strong>Output:</strong> true
<strong>Explanation: </strong>2 and 3 sum up to 5.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="./assets/image2.png" style="width: 453px; height: 290px;" />
<pre>
<strong>Input:</strong> root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in each tree is in the range <code>[1, 5000]</code>.</li>
	<li><code>-10<sup>9</sup> &lt;= Node.val, target &lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Two Pointers`
-	`Binary Search`
-	`Stack`
-	`Tree`
-	`Depth-First Search`
-	`Binary Search Tree`
-	`Binary Tree`

</details>


<details>
<summary> Hint 1 </summary>
How can you reduce this problem to the classical Two Sum problem?
</details>

<details>
<summary> Hint 2 </summary>
Do an in-order traversal of each tree to convert them to sorted arrays.
</details>

<details>
<summary> Hint 3 </summary>
Solve the classical Two Sum problem.
</details>
