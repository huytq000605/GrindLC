
# 2845. Count of Interesting Subarrays<br> Medium

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>, an integer <code>modulo</code>, and an integer <code>k</code>.</p>

<p>Your task is to find the count of subarrays that are <strong>interesting</strong>.</p>

<p>A <strong>subarray</strong> <code>nums[l..r]</code> is <strong>interesting</strong> if the following condition holds:</p>

<ul>
	<li>Let <code>cnt</code> be the number of indices <code>i</code> in the range <code>[l, r]</code> such that <code>nums[i] % modulo == k</code>. Then, <code>cnt % modulo == k</code>.</li>
</ul>

<p>Return <em>an integer denoting the count of interesting subarrays. </em></p>

<p><span><strong>Note:</strong> A subarray is <em>a contiguous non-empty sequence of elements within an array</em>.</span></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,4], modulo = 2, k = 1
<strong>Output:</strong> 3
<strong>Explanation:</strong> In this example the interesting subarrays are: 
The subarray nums[0..0] which is [3]. 
- There is only one index, i = 0, in the range [0, 0] that satisfies nums[i] % modulo == k. 
- Hence, cnt = 1 and cnt % modulo == k.  
The subarray nums[0..1] which is [3,2].
- There is only one index, i = 0, in the range [0, 1] that satisfies nums[i] % modulo == k.  
- Hence, cnt = 1 and cnt % modulo == k.
The subarray nums[0..2] which is [3,2,4]. 
- There is only one index, i = 0, in the range [0, 2] that satisfies nums[i] % modulo == k. 
- Hence, cnt = 1 and cnt % modulo == k. 
It can be shown that there are no other interesting subarrays. So, the answer is 3.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,9,6], modulo = 3, k = 0
<strong>Output:</strong> 2
<strong>Explanation: </strong>In this example the interesting subarrays are: 
The subarray nums[0..3] which is [3,1,9,6]. 
- There are three indices, i = 0, 2, 3, in the range [0, 3] that satisfy nums[i] % modulo == k. 
- Hence, cnt = 3 and cnt % modulo == k. 
The subarray nums[1..1] which is [1]. 
- There is no index, i, in the range [1, 1] that satisfies nums[i] % modulo == k. 
- Hence, cnt = 0 and cnt % modulo == k. 
It can be shown that there are no other interesting subarrays. So, the answer is 2.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5 </sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= modulo &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt; modulo</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Hash Table`
-	`Prefix Sum`

</details>


<details>
<summary> Hint 1 </summary>
The problem can be solved using prefix sums.
</details>

<details>
<summary> Hint 2 </summary>
Let <code>count[i]</code> be the number of indices where <code>nums[i] % modulo == k</code> among the first <code>i</code> indices.
</details>

<details>
<summary> Hint 3 </summary>
<code>count[0] = 0</code> and <code>count[i] = count[i - 1] + (nums[i - 1] % modulo == k ? 1 : 0)</code> for <code>i = 1, 2, ..., n</code>.
</details>

<details>
<summary> Hint 4 </summary>
Now we want to calculate for each <code>i = 1, 2, ..., n</code>, how many indices <code>j < i</code> such that <code>(count[i] - count[j]) % modulo == k</code>.
</details>

<details>
<summary> Hint 5 </summary>
Rewriting <code>(count[i] - count[j]) % modulo == k</code> becomes <code>count[j] = (count[i] + modulo - k) % modulo</code>.
</details>

<details>
<summary> Hint 6 </summary>
Using a map data structure, for each <code>i = 0, 1, 2, ..., n</code>, we just sum up all <code>map[(count[i] + modulo - k) % modulo]</code> before increasing <code>map[count[i] % modulo]</code>, and the total sum is the final answer.
</details>