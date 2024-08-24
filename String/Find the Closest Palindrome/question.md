
# 564. Find the Closest Palindrome<br> Hard

<p>Given a string <code>n</code> representing an integer, return <em>the closest integer (not including itself), which is a palindrome</em>. If there is a tie, return <em><strong>the smaller one</strong></em>.</p>

<p>The closest is defined as the absolute difference minimized between two integers.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;123&quot;
<strong>Output:</strong> &quot;121&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = &quot;1&quot;
<strong>Output:</strong> &quot;0&quot;
<strong>Explanation:</strong> 0 and 2 are the closest palindromes but we return the smallest which is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n.length &lt;= 18</code></li>
	<li><code>n</code> consists of only digits.</li>
	<li><code>n</code> does not have leading zeros.</li>
	<li><code>n</code> is representing an integer in the range <code>[1, 10<sup>18</sup> - 1]</code>.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Math`
-	`String`

</details>


<details>
<summary> Hint 1 </summary>
Will brute force work for this problem? Think of something else.
</details>

<details>
<summary> Hint 2 </summary>
Take some examples like 1234, 999,1000, etc and check their closest palindromes. How many different cases are possible?
</details>

<details>
<summary> Hint 3 </summary>
Do we have to consider only left half or right half of the string or both?
</details>

<details>
<summary> Hint 4 </summary>
Try to find the closest palindrome of these numbers- 12932, 99800, 12120. Did you observe something?
</details>