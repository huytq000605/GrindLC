
# 1885. Count Pairs in Two Arrays<br> Medium

<p>Given two integer arrays <code>nums1</code> and <code>nums2</code> of length <code>n</code>, count the pairs of indices <code>(i, j)</code> such that <code>i &lt; j</code> and <code>nums1[i] + nums1[j] &gt; nums2[i] + nums2[j]</code>.</p>

<p>Return <em>the <strong>number of pairs</strong> satisfying the condition.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [2,1,2,1], nums2 = [1,2,1,2]
<strong>Output:</strong> 1
<strong>Explanation</strong>: The pairs satisfying the condition are:
- (0, 2) where 2 + 2 &gt; 1 + 1.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums1 = [1,10,6,2], nums2 = [1,4,1,5]
<strong>Output:</strong> 5
<strong>Explanation</strong>: The pairs satisfying the condition are:
- (0, 1) where 1 + 10 &gt; 1 + 4.
- (0, 2) where 1 + 6 &gt; 1 + 1.
- (1, 2) where 10 + 6 &gt; 4 + 1.
- (1, 3) where 10 + 2 &gt; 4 + 5.
- (2, 3) where 6 + 2 &gt; 1 + 5.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums1.length == nums2.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums1[i], nums2[i] &lt;= 10<sup>5</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Two Pointers`
-	`Binary Search`
-	`Sorting`

</details>


<details>
<summary> Hint 1 </summary>
We can write it as nums1[i] - nums2[i] > nums2[j] - nums1[j] instead of nums1[i] + nums1[j] > nums2[i] + nums2[j].
</details>

<details>
<summary> Hint 2 </summary>
Store nums1[idx] - nums2[idx] in a data structure.
</details>

<details>
<summary> Hint 3 </summary>
Store nums2[idx] - nums1[idx] in a different data structure.
</details>

<details>
<summary> Hint 4 </summary>
For each integer in the first data structure, count the number of the strictly smaller integers in the second data structure with a larger index in the original array.
</details>