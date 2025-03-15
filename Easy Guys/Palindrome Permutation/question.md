
# 266. Palindrome Permutation<br> Easy

<p>Given a string <code>s</code>, return <code>true</code> <em>if a permutation of the string could form a </em><span data-keyword="palindrome-string"><em><strong>palindrome</strong></em></span><em> and </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;code&quot;
<strong>Output:</strong> false
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aab&quot;
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;carerac&quot;
<strong>Output:</strong> true
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 5000</code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Hash Table`
-	`String`
-	`Bit Manipulation`

</details>


<details>
<summary> Hint 1 </summary>
Consider the palindromes of odd vs even length. What difference do you notice?
</details>

<details>
<summary> Hint 2 </summary>
Count the frequency of each character.
</details>

<details>
<summary> Hint 3 </summary>
If each character occurs even number of times, then it must be a palindrome. How about character which occurs odd number of times?
</details>