
# 3185. Count Pairs That Form a Complete Day II<br> Medium

<p>Given an integer array <code>hours</code> representing times in <strong>hours</strong>, return an integer denoting the number of pairs <code>i</code>, <code>j</code> where <code>i &lt; j</code> and <code>hours[i] + hours[j]</code> forms a <strong>complete day</strong>.</p>

<p>A <strong>complete day</strong> is defined as a time duration that is an <strong>exact</strong> <strong>multiple</strong> of 24 hours.</p>

<p>For example, 1 day is 24 hours, 2 days is 48 hours, 3 days is 72 hours, and so on.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">hours = [12,12,30,24,24]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong> The pairs of indices that form a complete day are <code>(0, 1)</code> and <code>(3, 4)</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">hours = [72,48,24,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong> The pairs of indices that form a complete day are <code>(0, 1)</code>, <code>(0, 2)</code>, and <code>(1, 2)</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= hours.length &lt;= 5 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= hours[i] &lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Hash Table`
-	`Counting`

</details>


<details>
<summary> Hint 1 </summary>
A pair <code>(i, j)</code> forms a valid complete day if <code>(hours[i] + hours[j]) % 24 == 0</code>.
</details>

<details>
<summary> Hint 2 </summary>
Using an array or a map, for each index <code>j</code> moving from left to right, increase the answer by the count of <code>(24 - hours[j]) % 24</code>, and then increase the count of <code>hours[j]</code>.
</details>