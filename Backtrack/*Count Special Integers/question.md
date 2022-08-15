
# 2376. Count Special Integers<br> Hard

<p>We call a positive integer <strong>special</strong> if all of its digits are <strong>distinct</strong>.</p>

<p>Given a <strong>positive</strong> integer <code>n</code>, return <em>the number of special integers that belong to the interval </em><code>[1, n]</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 20
<strong>Output:</strong> 19
<strong>Explanation:</strong> All the integers from 1 to 20, except 11, are special. Thus, there are 19 special integers.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 5
<strong>Explanation:</strong> All the integers from 1 to 5 are special.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 135
<strong>Output:</strong> 110
<strong>Explanation:</strong> There are 110 integers from 1 to 135 that are special.
Some of the integers that are not special are: 22, 114, and 131.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 2 * 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
Try to think of dynamic programming.
</details>

<details>
<summary> Hint 2 </summary>
Use the idea of digit dynamic programming to build the numbers, in addition to a bitmask that will tell which digits you have used so far on the number that you are building.
</details>