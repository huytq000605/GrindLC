
# 2471. Minimum Number of Operations to Sort a Binary Tree by Level<br> Medium

<p>You are given the <code>root</code> of a binary tree with <strong>unique values</strong>.</p>

<p>In one operation, you can choose any two nodes <strong>at the same level</strong> and swap their values.</p>

<p>Return <em>the minimum number of operations needed to make the values at each level sorted in a <strong>strictly increasing order</strong></em>.</p>

<p>The <strong>level</strong> of a node is the number of edges along the path between it and the root node<em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img src="./assets/image1.png" style="width: 500px; height: 324px;" />
<pre>
<strong>Input:</strong> root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
- Swap 4 and 3. The 2<sup>nd</sup> level becomes [3,4].
- Swap 7 and 5. The 3<sup>rd</sup> level becomes [5,6,8,7].
- Swap 8 and 7. The 3<sup>rd</sup> level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img src="./assets/image2.png" style="width: 400px; height: 303px;" />
<pre>
<strong>Input:</strong> root = [1,3,2,7,6,5,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
- Swap 3 and 2. The 2<sup>nd</sup> level becomes [2,3].
- Swap 7 and 4. The 3<sup>rd</sup> level becomes [4,6,5,7].
- Swap 6 and 5. The 3<sup>rd</sup> level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img src="./assets/image3.png" style="width: 400px; height: 274px;" />
<pre>
<strong>Input:</strong> root = [1,2,3,4,5,6]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Each level is already sorted in increasing order so return 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li>All the values of the tree are <strong>unique</strong>.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Tree`
-	`Breadth-First Search`
-	`Binary Tree`

</details>


<details>
<summary> Hint 1 </summary>
We can group the values level by level and solve each group independently.
</details>

<details>
<summary> Hint 2 </summary>
Do BFS to group the value level by level.
</details>

<details>
<summary> Hint 3 </summary>
Find the minimum number of swaps to sort the array of each level.
</details>

<details>
<summary> Hint 4 </summary>
While iterating over the array, check the current element, and if not in the correct index, replace that element with the index of the element which should have come.
</details>