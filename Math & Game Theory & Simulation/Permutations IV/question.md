
# 3470. Permutations IV<br> Hard

<p>Given two integers, <code>n</code> and <code>k</code>, an <strong>alternating permutation</strong> is a permutation of the first <code>n</code> positive integers such that no <strong>two</strong> adjacent elements are both odd or both even.</p>

<p>Return the <strong>k-th</strong> <strong>alternating permutation</strong> sorted in <em>lexicographical order</em>. If there are fewer than <code>k</code> valid <strong>alternating permutations</strong>, return an empty list.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 4, k = 6</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,4,1,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The lexicographically-sorted alternating permutations of <code>[1, 2, 3, 4]</code> are:</p>

<ol>
	<li><code>[1, 2, 3, 4]</code></li>
	<li><code>[1, 4, 3, 2]</code></li>
	<li><code>[2, 1, 4, 3]</code></li>
	<li><code>[2, 3, 4, 1]</code></li>
	<li><code>[3, 2, 1, 4]</code></li>
	<li><code>[3, 4, 1, 2]</code> &larr; 6th permutation</li>
	<li><code>[4, 1, 2, 3]</code></li>
	<li><code>[4, 3, 2, 1]</code></li>
</ol>

<p>Since <code>k = 6</code>, we return <code>[3, 4, 1, 2]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">[3,2,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>The lexicographically-sorted alternating permutations of <code>[1, 2, 3]</code> are:</p>

<ol>
	<li><code>[1, 2, 3]</code></li>
	<li><code>[3, 2, 1]</code> &larr; 2nd permutation</li>
</ol>

<p>Since <code>k = 2</code>, we return <code>[3, 2, 1]</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>

<p><strong>Explanation:</strong></p>

<p>The lexicographically-sorted alternating permutations of <code>[1, 2]</code> are:</p>

<ol>
	<li><code>[1, 2]</code></li>
	<li><code>[2, 1]</code></li>
</ol>

<p>There are only 2 alternating permutations, but <code>k = 3</code>, which is out of range. Thus, we return an empty list <code>[]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>15</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Math`
-	`Combinatorics`
-	`Enumeration`

</details>


<details>
<summary> Hint 1 </summary>
If <code>n</code> is odd, the first number must be odd.
</details>

<details>
<summary> Hint 2 </summary>
If <code>n</code> is even, the first number can be either odd or even.
</details>

<details>
<summary> Hint 3 </summary>
From smallest to largest, place each number and subtract the number of permutations from <code>k</code>.
</details>

<details>
<summary> Hint 4 </summary>
The number of permutations can be calculated using factorials.
</details>