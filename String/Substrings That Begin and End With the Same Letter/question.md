
# 2083. Substrings That Begin and End With the Same Letter<br> Medium

<p>You are given a <strong>0-indexed</strong> string <code>s</code> consisting of only lowercase English letters. Return <em>the number of <strong>substrings</strong> in </em><code>s</code> <em>that begin and end with the <strong>same</strong> character.</em></p>

<p>A <strong>substring</strong> is a contiguous non-empty sequence of characters within a string.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcba&quot;
<strong>Output:</strong> 7
<strong>Explanation:</strong>
The substrings of length 1 that start and end with the same letter are: &quot;a&quot;, &quot;b&quot;, &quot;c&quot;, &quot;b&quot;, and &quot;a&quot;.
The substring of length 3 that starts and ends with the same letter is: &quot;bcb&quot;.
The substring of length 5 that starts and ends with the same letter is: &quot;abcba&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abacad&quot;
<strong>Output:</strong> 9
<strong>Explanation:</strong>
The substrings of length 1 that start and end with the same letter are: &quot;a&quot;, &quot;b&quot;, &quot;a&quot;, &quot;c&quot;, &quot;a&quot;, and &quot;d&quot;.
The substrings of length 3 that start and end with the same letter are: &quot;aba&quot; and &quot;aca&quot;.
The substring of length 5 that starts and ends with the same letter is: &quot;abaca&quot;.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;
<strong>Output:</strong> 1
<strong>Explanation:</strong>
The substring of length 1 that starts and ends with the same letter is: &quot;a&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Hash Table`
-	`Math`
-	`String`
-	`Counting`
-	`Prefix Sum`

</details>


<details>
<summary> Hint 1 </summary>
In the string "abacad", the letter "a" appears 3 times. How many substrings begin with the first "a" and end with any "a"?
</details>

<details>
<summary> Hint 2 </summary>
There are 3 substrings ("a", "aba", and "abaca"). How many substrings begin with the second "a" and end with any "a"? How about the third?
</details>

<details>
<summary> Hint 3 </summary>
2 substrings begin with the second "a" ("a", and "aca") and 1 substring begins with the third "a" ("a").
</details>

<details>
<summary> Hint 4 </summary>
There is a total of 3 + 2 + 1 = 6 substrings that begin and end with "a".
</details>

<details>
<summary> Hint 5 </summary>
If a character appears i times in the string, there are i * (i + 1) / 2 substrings that begin and end with that character.
</details>