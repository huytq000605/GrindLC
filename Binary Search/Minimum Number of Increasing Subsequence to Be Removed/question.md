
# 3231. Minimum Number of Increasing Subsequence to Be Removed<br> Hard

<p>Given an array of integers <code>nums</code>, you are allowed to perform the following operation any number of times:</p>

<ul>
	<li>Remove a <strong>strictly increasing</strong> <span data-keyword="subsequence-array">subsequence</span> from the array.</li>
</ul>

<p>Your task is to find the <strong>minimum</strong> number of operations required to make the array <strong>empty</strong>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,3,1,4,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>We remove subsequences <code>[1, 2]</code>, <code>[3, 4]</code>, <code>[5]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5,4,3,2,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
Find the longest non-increasing subsequence.
</details>

<details>
<summary> Hint 2 </summary>
No two elements of this sequence can be removed in one operation.
</details>

<details>
<summary> Hint 3 </summary>
Try to prove that the answer is equal to the length of this sequence.
</details>