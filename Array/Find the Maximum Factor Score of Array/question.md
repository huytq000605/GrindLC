
# 3334. Find the Maximum Factor Score of Array<br> Medium

<p>You are given an integer array <code>nums</code>.</p>

<p>The <strong>factor score</strong> of an array is defined as the <em>product</em> of the LCM and GCD of all elements of that array.</p>

<p>Return the <strong>maximum factor score</strong> of <code>nums</code> after removing <strong>at most</strong> one element from it.</p>

<p><strong>Note</strong> that <em>both</em> the <span data-keyword="lcm-function">LCM</span> and <span data-keyword="gcd-function">GCD</span> of a single number are the number itself, and the <em>factor score</em> of an <strong>empty</strong> array is 0.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,4,8,16]</span></p>

<p><strong>Output:</strong> <span class="example-io">64</span></p>

<p><strong>Explanation:</strong></p>

<p>On removing 2, the GCD of the rest of the elements is 4 while the LCM is 16, which gives a maximum factor score of <code>4 * 16 = 64</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">60</span></p>

<p><strong>Explanation:</strong></p>

<p>The maximum factor score of 60 can be obtained without removing any elements.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3]</span></p>

<p><strong>Output:</strong> 9</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 30</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Math`
-	`Number Theory`

</details>


<details>
<summary> Hint 1 </summary>
Use brute force approach with two loops.
</details>

<details>
<summary> Hint 2 </summary>
Optimize using prefix and suffix arrays.
</details>