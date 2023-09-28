
# 2856. Minimum Array Length After Pair Removals<br> Medium

<p>You are given a <strong>0-indexed</strong> <strong>sorted</strong> array of integers <code>nums</code>.</p>

<p>You can perform the following operation any number of times:</p>

<ul>
	<li>Choose <strong>two</strong> indices, <code>i</code> and <code>j</code>, where <code>i &lt; j</code>, such that <code>nums[i] &lt; nums[j]</code>.</li>
	<li>Then, remove the elements at indices <code>i</code> and <code>j</code> from <code>nums</code>. The remaining elements retain their original order, and the array is re-indexed.</li>
</ul>

<p>Return <em>an integer that denotes the <strong>minimum</strong> length of </em><code>nums</code><em> after performing the operation any number of times (<strong>including zero</strong>).</em></p>

<p>Note that <code>nums</code> is sorted in <strong>non-decreasing</strong> order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,4,9]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Initially, nums = [1, 3, 4, 9].
In the first operation, we can choose index 0 and 1 because nums[0] &lt; nums[1] &lt;=&gt; 1 &lt; 3.
Remove indices 0 and 1, and nums becomes [4, 9].
For the next operation, we can choose index 0 and 1 because nums[0] &lt; nums[1] &lt;=&gt; 4 &lt; 9.
Remove indices 0 and 1, and nums becomes an empty array [].
Hence, the minimum length achievable is 0.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,6,9]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Initially, nums = [2, 3, 6, 9]. 
In the first operation, we can choose index 0 and 2 because nums[0] &lt; nums[2] &lt;=&gt; 2 &lt; 6. 
Remove indices 0 and 2, and nums becomes [3, 9]. 
For the next operation, we can choose index 0 and 1 because nums[0] &lt; nums[1] &lt;=&gt; 3 &lt; 9. 
Remove indices 0 and 1, and nums becomes an empty array []. 
Hence, the minimum length achievable is 0.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Initially, nums = [1, 1, 2].
In an operation, we can choose index 0 and 2 because nums[0] &lt; nums[2] &lt;=&gt; 1 &lt; 2. 
Remove indices 0 and 2, and nums becomes [1]. 
It is no longer possible to perform an operation on the array. 
Hence, the minimum achievable length is 1. 
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is sorted in <strong>non-decreasing</strong> order.</li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
To minimize the length of the array, we should maximize the number of operations performed.
</details>

<details>
<summary> Hint 2 </summary>
To perform <code>k</code> operations, it is optimal to use the smallest <code>k</code> values and the largest <code>k</code> values in <code>nums</code>.
</details>

<details>
<summary> Hint 3 </summary>
What is the best way to make pairs from the smallest <code>k</code> values and the largest <code>k</code> values so it is possible to remove all the pairs?
</details>

<details>
<summary> Hint 4 </summary>
If we consider the smallest <code>k</code> values and the largest <code>k</code> values as two separate <strong>sorted 0-indexed</strong> arrays, <code>a</code> and <code>b</code>, It is optimal to pair <code>a[i]</code> and <code>b[i]</code>. So, a <code>k</code> is valid if <code>a[i] < b[i]</code> for all <code>i</code> in the range <code>[0, k - 1]</code>.
</details>

<details>
<summary> Hint 5 </summary>
The greatest possible valid <code>k</code> can be found using binary search.
</details>

<details>
<summary> Hint 6 </summary>
The answer is <code>nums.length - 2 * k</code>.
</details>