
# 2357. Make Array Zero by Subtracting Equal Amounts<br> Easy

<p>You are given a non-negative integer array <code>nums</code>. In one operation, you must:</p>

<ul>
	<li>Choose a positive integer <code>x</code> such that <code>x</code> is less than or equal to the <strong>smallest non-zero</strong> element in <code>nums</code>.</li>
	<li>Subtract <code>x</code> from every <strong>positive</strong> element in <code>nums</code>.</li>
</ul>

<p>Return <em>the <strong>minimum</strong> number of operations to make every element in </em><code>nums</code><em> equal to </em><code>0</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,5,0,3,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong>
In the first operation, choose x = 1. Now, nums = [0,4,0,2,4].
In the second operation, choose x = 2. Now, nums = [0,2,0,0,2].
In the third operation, choose x = 2. Now, nums = [0,0,0,0,0].
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [0]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Each element in nums is already 0 so no operations are needed.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 100</code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
It is always best to set x as the smallest non-zero element in nums.
</details>

<details>
<summary> Hint 2 </summary>
Elements with the same value will always take the same number of operations to become 0. Contrarily, elements with different values will always take a different number of operations to become 0.
</details>

<details>
<summary> Hint 3 </summary>
The answer is the number of unique non-zero numbers in nums.
</details>