
# 3171. Find Subarray With Bitwise AND Closest to K<br> Hard

<p>You are given an array <code>nums</code> and an integer <code>k</code>. You need to find a <span data-keyword="subarray-nonempty">subarray</span> of <code>nums</code> such that the <strong>absolute difference</strong> between <code>k</code> and the bitwise <code>AND</code> of the subarray elements is as<strong> small</strong> as possible. In other words, select a subarray <code>nums[l..r]</code> such that <code>|k - (nums[l] AND nums[l + 1] ... AND nums[r])|</code> is minimum.</p>

<p>Return the <strong>minimum</strong> possible value of the absolute difference.</p>

<p>A <strong>subarray</strong> is a contiguous <b>non-empty</b> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,4,5], k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>The subarray <code>nums[2..3]</code> has <code>AND</code> value 4, which gives the minimum absolute difference <code>|3 - 4| = 1</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,1,2], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The subarray <code>nums[1..1]</code> has <code>AND</code> value 2, which gives the minimum absolute difference <code>|2 - 2| = 0</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1], k = 10</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>There is a single subarray with <code>AND</code> value 1, which gives the minimum absolute difference <code>|10 - 1| = 9</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Binary Search`
-	`Bit Manipulation`
-	`Segment Tree`

</details>


<details>
<summary> Hint 1 </summary>
Let <code>dp[i]</code> be the set of all the bitwise <code>AND</code> of all the subarrays ending at index <code>i</code>.
</details>

<details>
<summary> Hint 2 </summary>
We start from <code>nums[i]</code>, taking the bitwise <code>AND</code> result by including elements one by one from <code>i</code> towards left. Notice that only set bits can become unset on adding a element, and unset bits never become set again.
</details>

<details>
<summary> Hint 3 </summary>
Hence <code>dp[i]</code> can contain at most 30 elements.
</details>