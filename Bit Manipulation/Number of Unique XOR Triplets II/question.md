
# 3514. Number of Unique XOR Triplets II<br> Medium

<p data-end="261" data-start="147">You are given an integer array <code>nums</code>.</p>

<p>A <strong>XOR triplet</strong> is defined as the XOR of three elements <code>nums[i] XOR nums[j] XOR nums[k]</code> where <code>i &lt;= j &lt;= k</code>.</p>

<p>Return the number of <strong>unique</strong> XOR triplet values from all possible triplets <code>(i, j, k)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p data-end="158" data-start="101">The possible XOR triplet values are:</p>

<ul data-end="280" data-start="159">
	<li data-end="188" data-start="159"><code>(0, 0, 0) &rarr; 1 XOR 1 XOR 1 = 1</code></li>
	<li data-end="218" data-start="189"><code>(0, 0, 1) &rarr; 1 XOR 1 XOR 3 = 3</code></li>
	<li data-end="248" data-start="219"><code>(0, 1, 1) &rarr; 1 XOR 3 XOR 3 = 1</code></li>
	<li data-end="280" data-start="249"><code>(1, 1, 1) &rarr; 3 XOR 3 XOR 3 = 3</code></li>
</ul>

<p data-end="343" data-start="282">The unique XOR values are <code data-end="316" data-start="308">{1, 3}</code>. Thus, the output is 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [6,7,8,9]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The possible XOR triplet values are <code data-end="275" data-start="267">{6, 7, 8, 9}</code>. Thus, the output is 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1500</code></li>
	<li><code><font face="monospace">1 &lt;= nums[i] &lt;= 1500</font></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Math`
-	`Bit Manipulation`
-	`Enumeration`

</details>


<details>
<summary> Hint 1 </summary>
What is the maximum possible XOR value achievable by any triplet?
</details>

<details>
<summary> Hint 2 </summary>
Let the maximum possible XOR value be stored in <code>max_xor</code>.
</details>

<details>
<summary> Hint 3 </summary>
For each index <code>i</code>, consider all pairs of indices <code>(j, k)</code> such that <code>i <= j <= k</code>. For each such pair, compute the triplet XOR as <code>nums[i] XOR nums[j] XOR nums[k]</code>.
</details>

<details>
<summary> Hint 4 </summary>
You can optimize the calculation by precomputing or reusing intermediate XOR results. For example, after fixing an index <code>i</code>, compute XORs of pairs <code>(j, k)</code> in <code>O(n<sup>2</sup>)</code> time instead of checking all three indices independently.
</details>

<details>
<summary> Hint 5 </summary>
Finally, count the number of unique XOR values obtained from all triplets.
</details>