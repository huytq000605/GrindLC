
# 3164. Find the Number of Good Pairs II<br> Medium

<p>You are given 2 integer arrays <code>nums1</code> and <code>nums2</code> of lengths <code>n</code> and <code>m</code> respectively. You are also given a <strong>positive</strong> integer <code>k</code>.</p>

<p>A pair <code>(i, j)</code> is called <strong>good</strong> if <code>nums1[i]</code> is divisible by <code>nums2[j] * k</code> (<code>0 &lt;= i &lt;= n - 1</code>, <code>0 &lt;= j &lt;= m - 1</code>).</p>

<p>Return the total number of <strong>good</strong> pairs.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [1,3,4], nums2 = [1,3,4], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>
The 5 good pairs are <code>(0, 0)</code>, <code>(1, 0)</code>, <code>(1, 1)</code>, <code>(2, 0)</code>, and <code>(2, 2)</code>.</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums1 = [1,2,4,12], nums2 = [2,4], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The 2 good pairs are <code>(3, 0)</code> and <code>(3, 1)</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, m &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[j] &lt;= 10<sup>6</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>3</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Hash Table`

</details>


<details>
<summary> Hint 1 </summary>
Let <code>f[v]</code> be the number of occurrences of <code>v/k</code> in nums2.
</details>

<details>
<summary> Hint 2 </summary>
For each value <code>v</code> in nums1, enumerating all its factors <code>d</code> (in <code>sqrt(v)</code> time) and sum up all the <code>f[d]</code> to get the final answer.
</details>

<details>
<summary> Hint 3 </summary>
It is also possible to improve the complexity from <code>v * sqrt(v)</code> to <code>v * log(v)</code> - How?
</details>