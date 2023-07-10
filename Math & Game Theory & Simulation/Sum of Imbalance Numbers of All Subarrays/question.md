
# 2763. Sum of Imbalance Numbers of All Subarrays<br> Hard

<p>The <strong>imbalance number</strong> of a <strong>0-indexed</strong> integer array <code>arr</code> of length <code>n</code> is defined as the number of indices in <code>sarr = sorted(arr)</code> such that:</p>

<ul>
	<li><code>0 &lt;= i &lt; n - 1</code>, and</li>
	<li><code>sarr[i+1] - sarr[i] &gt; 1</code></li>
</ul>

<p>Here, <code>sorted(arr)</code> is the function that returns the sorted version of <code>arr</code>.</p>

<p>Given a <strong>0-indexed</strong> integer array <code>nums</code>, return <em>the <strong>sum of imbalance numbers</strong> of all its <strong>subarrays</strong></em>.</p>

<p>A <strong>subarray</strong> is a contiguous <strong>non-empty</strong> sequence of elements within an array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,1,4]
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are 3 subarrays with non-zero<strong> </strong>imbalance numbers:
- Subarray [3, 1] with an imbalance number of 1.
- Subarray [3, 1, 4] with an imbalance number of 1.
- Subarray [1, 4] with an imbalance number of 1.
The imbalance number of all other subarrays is 0. Hence, the sum of imbalance numbers of all the subarrays of nums is 3. 
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,3,3,3,5]
<strong>Output:</strong> 8
<strong>Explanation:</strong> There are 7 subarrays with non-zero imbalance numbers:
- Subarray [1, 3] with an imbalance number of 1.
- Subarray [1, 3, 3] with an imbalance number of 1.
- Subarray [1, 3, 3, 3] with an imbalance number of 1.
- Subarray [1, 3, 3, 3, 5] with an imbalance number of 2. 
- Subarray [3, 3, 3, 5] with an imbalance number of 1. 
- Subarray [3, 3, 5] with an imbalance number of 1.
- Subarray [3, 5] with an imbalance number of 1.
The imbalance number of all other subarrays is 0. Hence, the sum of imbalance numbers of all the subarrays of nums is 8. </pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= nums.length</code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
Iterate over all subarrays in a nested fashion. Namely, for each left endpoint, start from nums[left] and add elements nums[left + 1], nums[left + 2], etc.
</details>

<details>
<summary> Hint 2 </summary>
To keep track of the imbalance value, maintain a set of added elements.
</details>

<details>
<summary> Hint 3 </summary>
Increment the imbalance value whenever a new number is not adjacent (+/- 1) to other old numbers. For example, when you add 3 to [1, 5], or when you add 5 to [1, 3]. For a formal proof, consider three cases: new value is (i) largest, (ii) smallest, (iii) between two old numbers.
</details>

<details>
<summary> Hint 4 </summary>
Decrement the imbalance value whenever a new number is adjacent (+/- 1) to two old numbers. For example, when you add 3 to [2, 4]. The imbalance value does not change in the case of one adjacent old number.
</details>