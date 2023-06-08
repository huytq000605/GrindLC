
# 1150. Check If a Number Is Majority Element in a Sorted Array<br> Easy

<p>Given an integer array <code>nums</code> sorted in non-decreasing order and an integer <code>target</code>, return <code>true</code> <em>if</em> <code>target</code> <em>is a <strong>majority</strong> element, or </em><code>false</code><em> otherwise</em>.</p>

<p>A <strong>majority</strong> element in an array <code>nums</code> is an element that appears more than <code>nums.length / 2</code> times in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,4,5,5,5,5,5,6,6], target = 5
<strong>Output:</strong> true
<strong>Explanation:</strong> The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 &gt; 9/2 is true.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,100,101,101], target = 101
<strong>Output:</strong> false
<strong>Explanation:</strong> The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 &gt; 4/2 is false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i], target &lt;= 10<sup>9</sup></code></li>
	<li><code>nums</code> is sorted in non-decreasing order.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Binary Search`

</details>


<details>
<summary> Hint 1 </summary>
How to check if a given number target is a majority element?.
</details>

<details>
<summary> Hint 2 </summary>
Find the frequency of target and compare it to the length of the array.
</details>

<details>
<summary> Hint 3 </summary>
You can find the frequency of an element using Binary Search since the array is sorted.
</details>

<details>
<summary> Hint 4 </summary>
Using Binary Search, find the first and last occurrences of A. Then just calculate the difference between the indexes of these occurrences.
</details>