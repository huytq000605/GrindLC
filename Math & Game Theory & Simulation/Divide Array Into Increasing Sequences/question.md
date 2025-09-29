
# 1121. Divide Array Into Increasing Sequences<br> Hard

<p>Given an integer array <code>nums</code> sorted in non-decreasing order and an integer <code>k</code>, return <code>true</code><em> if this array can be divided into one or more disjoint increasing subsequences of length at least </em><code>k</code><em>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,2,3,3,4,4], k = 3
<strong>Output:</strong> true
<strong>Explanation:</strong> The array can be divided into two subsequences [1,2,3,4] and [2,3,4] with lengths at least 3 each.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,6,6,7,8], k = 3
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no way to divide the array using the conditions required.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>nums</code> is sorted in non-decreasing order.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Counting`

</details>


<details>
<summary> Hint 1 </summary>
Think in the frequency of the numbers and how this affects the number of sequences needed.
</details>

<details>
<summary> Hint 2 </summary>
What is the minimum number of sequences we need to form? Considering frequency of the numbers.
</details>

<details>
<summary> Hint 3 </summary>
Think about the least number of sequences to maximize the lengths.
</details>

<details>
<summary> Hint 4 </summary>
The number of sequences needed is equal to the maximum frequency of an element.
</details>

<details>
<summary> Hint 5 </summary>
How to put the other elements into sequences ? Think in a greedy approach.
</details>