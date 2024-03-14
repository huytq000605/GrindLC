
# 2393. Count Strictly Increasing Subarrays<br> Medium

<p>You are given an array <code>nums</code> consisting of <strong>positive</strong> integers.</p>

<p>Return <em>the number of <strong>subarrays</strong> of </em><code>nums</code><em> that are in <strong>strictly increasing</strong> order.</em></p>

<p>A <strong>subarray</strong> is a <strong>contiguous</strong> part of an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,5,4,4,6]
<strong>Output:</strong> 10
<strong>Explanation:</strong> The strictly increasing subarrays are the following:
- Subarrays of length 1: [1], [3], [5], [4], [4], [6].
- Subarrays of length 2: [1,3], [3,5], [4,6].
- Subarrays of length 3: [1,3,5].
The total number of subarrays is 6 + 3 + 1 = 10.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> 15
<strong>Explanation:</strong> Every subarray is strictly increasing. There are 15 possible subarrays that we can take.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Math`
-	`Dynamic Programming`

</details>


<details>
<summary> Hint 1 </summary>
Find the number of strictly increasing subarrays that end at a specific index. Can you calculate that for each index from 0 to n - 1?
</details>

<details>
<summary> Hint 2 </summary>
The answer will be the sum of the number of subarrays that end at each index.
</details>