
# 2413. Smallest Even Multiple<br> Easy

Given a <strong>positive</strong> integer <code>n</code>, return <em>the smallest positive integer that is a multiple of <strong>both</strong> </em><code>2</code><em> and </em><code>n</code>.
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 5
<strong>Output:</strong> 10
<strong>Explanation:</strong> The smallest multiple of both 5 and 2 is 10.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 6
<strong>Output:</strong> 6
<strong>Explanation:</strong> The smallest multiple of both 6 and 2 is 6. Note that a number is a multiple of itself.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 150</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Math`
-	`Number Theory`

</details>


<details>
<summary> Hint 1 </summary>
A guaranteed way to find a multiple of 2 and n is to multiply them together. When is this the answer, and when is there a smaller answer?
</details>

<details>
<summary> Hint 2 </summary>
There is a smaller answer when n is even.
</details>