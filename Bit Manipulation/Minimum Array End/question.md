
# 3133. Minimum Array End<br> Medium

<p>You are given two integers <code>n</code> and <code>x</code>. You have to construct an array of <strong>positive</strong> integers <code>nums</code> of size <code>n</code> where for every <code>0 &lt;= i &lt; n - 1</code>, <code>nums[i + 1]</code> is <strong>greater than</strong> <code>nums[i]</code>, and the result of the bitwise <code>AND</code> operation between all elements of <code>nums</code> is <code>x</code>.</p>

<p>Return the <strong>minimum</strong> possible value of <code>nums[n - 1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 3, x = 4</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p><code>nums</code> can be <code>[4,5,6]</code> and its last element is 6.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">n = 2, x = 7</span></p>

<p><strong>Output:</strong> <span class="example-io">15</span></p>

<p><strong>Explanation:</strong></p>

<p><code>nums</code> can be <code>[7,15]</code> and its last element is 15.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n, x &lt;= 10<sup>8</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Bit Manipulation`

</details>


<details>
<summary> Hint 1 </summary>
Each element of the array should be obtained by “merging” <code>x</code> and <code>v</code> where <code>v = 0, 1, 2, …(n - 1)</code>.
</details>

<details>
<summary> Hint 2 </summary>
To merge <code>x</code> with another number <code>v</code>, keep the set bits of <code>x</code> untouched, for all the other bits, fill the set bits of <code>v</code> from right to left in order one by one.
</details>

<details>
<summary> Hint 3 </summary>
So the final answer is the “merge” of <code>x</code> and <code>n - 1</code>.
</details>