
# 1295. Find Numbers with Even Number of Digits<br> Easy

<p>Given an array <code>nums</code> of integers, return how many of them contain an <strong>even number</strong> of digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [12,345,2,6,7896]
<strong>Output:</strong> 2
<strong>Explanation: 
</strong>12 contains 2 digits (even number of digits).&nbsp;
345 contains 3 digits (odd number of digits).&nbsp;
2 contains 1 digit (odd number of digits).&nbsp;
6 contains 1 digit (odd number of digits).&nbsp;
7896 contains 4 digits (even number of digits).&nbsp;
Therefore only 12 and 7896 contain an even number of digits.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [555,901,482,1771]
<strong>Output:</strong> 1 
<strong>Explanation: </strong>
Only 1771 contains an even number of digits.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 500</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Math`

</details>


<details>
<summary> Hint 1 </summary>
How to compute the number of digits of a number ?
</details>

<details>
<summary> Hint 2 </summary>
Divide the number by 10 again and again to get the number of digits.
</details>