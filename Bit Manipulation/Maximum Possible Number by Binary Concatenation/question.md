
# 3309. Maximum Possible Number by Binary Concatenation<br> Medium

<p>You are given an array of integers <code>nums</code> of size 3.</p>

<p>Return the <strong>maximum</strong> possible number whose <em>binary representation</em> can be formed by <strong>concatenating</strong> the <em>binary representation</em> of <strong>all</strong> elements in <code>nums</code> in some order.</p>

<p><strong>Note</strong> that the binary representation of any number <em>does not</em> contain leading zeros.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>Output:</strong> 30</p>

<p><strong>Explanation:</strong></p>

<p>Concatenate the numbers in the order <code>[3, 1, 2]</code> to get the result <code>&quot;11110&quot;</code>, which is the binary representation of 30.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,8,16]</span></p>

<p><strong>Output:</strong> 1296</p>

<p><strong>Explanation:</strong></p>

<p>Concatenate the numbers in the order <code>[2, 8, 16]</code> to get the result <code>&quot;10100010000&quot;</code>, which is the binary representation of 1296.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums.length == 3</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 127</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Bit Manipulation`
-	`Enumeration`

</details>


<details>
<summary> Hint 1 </summary>
How many possible concatenation orders are there?
</details>