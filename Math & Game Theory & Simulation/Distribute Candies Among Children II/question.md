
# 2929. Distribute Candies Among Children II<br> Medium

<p>You are given two positive integers <code>n</code> and <code>limit</code>.</p>

<p>Return <em>the <strong>total number</strong> of ways to distribute </em><code>n</code> <em>candies among </em><code>3</code><em> children such that no child gets more than </em><code>limit</code><em> candies.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5, limit = 2
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 ways to distribute 5 candies such that no child gets more than 2 candies: (1, 2, 2), (2, 1, 2) and (2, 2, 1).
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 3, limit = 3
<strong>Output:</strong> 10
<strong>Explanation:</strong> There are 10 ways to distribute 3 candies such that no child gets more than 3 candies: (0, 0, 3), (0, 1, 2), (0, 2, 1), (0, 3, 0), (1, 0, 2), (1, 1, 1), (1, 2, 0), (2, 0, 1), (2, 1, 0) and (3, 0, 0).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= limit &lt;= 10<sup>6</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Math`
-	`Combinatorics`
-	`Enumeration`

</details>


<details>
<summary> Hint 1 </summary>
We can enumerate the number of candies of one particular child, let it be <code>i</code> which means <code>0 <= i <= min(limit, n)</code>.
</details>

<details>
<summary> Hint 2 </summary>
Suppose the 2nd child gets <code>j</code> candies. Then <code>0 <= j <= limit</code> and <code>i + j <= n</code>.
</details>

<details>
<summary> Hint 3 </summary>
The 3rd child will hence get <code>n - i - j</code> candies and we should have <code>0 <= n - i - j <= limit</code>.
</details>

<details>
<summary> Hint 4 </summary>
After some transformations, for each <code>i</code>, we have <code>max(0, n - i - limit) <= j <= min(limit, n - i)</code>, each <code>j</code> corresponding to a solution.
So the number of solutions for some <code>i</code> is <code>max(min(limit, n - i) - max(0, n - i - limit) + 1, 0)</code>. Sum the expression for every <code>i</code> in <code>[0, min(n, limit)]</code>.
</details>