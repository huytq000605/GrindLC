
# 3209. Number of Subarrays With AND Value of K<br> Hard

<p>Given an array of integers <code>nums</code> and an integer <code>k</code>, return the number of <span data-keyword="subarray-nonempty">subarrays</span> of <code>nums</code> where the bitwise <code>AND</code> of the elements of the subarray equals <code>k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,1], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>All subarrays contain only 1&#39;s.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1,2], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Subarrays having an <code>AND</code> value of 1 are: <code>[<u><strong>1</strong></u>,1,2]</code>, <code>[1,<u><strong>1</strong></u>,2]</code>, <code>[<u><strong>1,1</strong></u>,2]</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Subarrays having an <code>AND</code> value of 2 are: <code>[1,<b><u>2</u></b>,3]</code>, <code>[1,<u><strong>2,3</strong></u>]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i], k &lt;= 10<sup>9</sup></code></li>
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
Let’s say we want to count the number of pairs <code>(l, r)</code> such that <code>nums[l] & nums[l + 1] & … & nums[r] == k</code>.
</details>

<details>
<summary> Hint 2 </summary>
Fix the left index <code>l</code>.
</details>

<details>
<summary> Hint 3 </summary>
Note that if you increase <code>r</code> for a fixed <code>l</code>, then the AND value of the subarray either decreases or remains unchanged.
</details>

<details>
<summary> Hint 4 </summary>
Therefore, consider using binary search.
</details>

<details>
<summary> Hint 5 </summary>
To calculate the AND value of a subarray, use sparse tables.
</details>