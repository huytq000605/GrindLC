
# 1133. Largest Unique Number<br> Easy

<p>Given an integer array <code>nums</code>, return <em>the largest integer that only occurs once</em>. If no integer occurs once, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,7,3,9,4,9,8,3,1]
<strong>Output:</strong> 8
<strong>Explanation:</strong> The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it is the answer.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [9,9,8,8]
<strong>Output:</strong> -1
<strong>Explanation:</strong> There is no number that occurs only once.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Hash Table`
-	`Sorting`

</details>


<details>
<summary> Hint 1 </summary>
Find the number of occurrences of each value.
</details>

<details>
<summary> Hint 2 </summary>
Use an array or a hash table to do that.
</details>

<details>
<summary> Hint 3 </summary>
Look for the largest value with number of occurrences = 1.
</details>
