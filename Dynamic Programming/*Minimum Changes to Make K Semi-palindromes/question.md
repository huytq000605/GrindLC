
# 2911. Minimum Changes to Make K Semi-palindromes<br> Hard

<p>Given a string <code>s</code> and an integer <code>k</code>, partition <code>s</code> into <code>k</code> <strong>substrings</strong> such that the sum of the number of letter changes required to turn each <strong>substring</strong> into a <strong>semi-palindrome</strong> is minimized.</p>

<p>Return <em>an integer denoting the <strong>minimum</strong> number of letter changes required.</em></p>

<p><strong>Notes</strong></p>

<ul>
	<li>A string is a <strong>palindrome</strong> if it can be read the same way from left to right and right to left.</li>
	<li>A string with a length of <code>len</code> is considered a <strong>semi-palindrome</strong> if there exists a positive integer <code>d</code> such that <code>1 &lt;= d &lt; len</code> and <code>len % d == 0</code>, and if we take indices that have the same modulo by <code>d</code>, they form a <strong>palindrome</strong>. For example, <code>&quot;aa&quot;</code>, <code>&quot;aba&quot;</code>, <code>&quot;adbgad&quot;</code>, and, <code>&quot;abab&quot;</code> are <strong>semi-palindrome</strong> and <code>&quot;a&quot;</code>, <code>&quot;ab&quot;</code>, and, <code>&quot;abca&quot;</code> are not.</li>
	<li>A <strong>substring</strong> is a contiguous sequence of characters within a string.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcac&quot;, k = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can divide s into substrings &quot;ab&quot; and &quot;cac&quot;. The string &quot;cac&quot; is already a semi-palindrome. If we change &quot;ab&quot; to &quot;aa&quot;, it becomes a semi-palindrome with d = 1.
It can be shown that there is no way to divide the string &quot;abcac&quot; into two semi-palindrome substrings. Therefore, the answer would be at least 1.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;abcdef&quot;, k = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can divide it into substrings &quot;abc&quot; and &quot;def&quot;. Each of the substrings &quot;abc&quot; and &quot;def&quot; requires one change to become a semi-palindrome, so we need 2 changes in total to make all substrings semi-palindrome.
It can be shown that we cannot divide the given string into two substrings in a way that it would require less than 2 changes.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;aabbaa&quot;, k = 3
<strong>Output:</strong> 0
<strong>Explanation:</strong> We can divide it into substrings &quot;aa&quot;, &quot;bb&quot; and &quot;aa&quot;.
The strings &quot;aa&quot; and &quot;bb&quot; are already semi-palindromes. Thus, the answer is zero.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 200</code></li>
	<li><code>1 &lt;= k &lt;= s.length / 2</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Two Pointers`
-	`String`
-	`Dynamic Programming`

</details>


<details>
<summary> Hint 1 </summary>
Define <code>dp[i][j]</code> as the minimum count of letter changes needed to split the suffix of string <code>s</code> starting from <code>s[i]</code> into <code>j</code> valid parts.
</details>

<details>
<summary> Hint 2 </summary>
We have <code>dp[i][j] = min(dp[x + 1][j - 1] + v[i][x])</code>. Here <code>v[i][x]</code> is the minimum number of letter changes to change substring <code>s[i..x]</code> into semi-palindrome.
</details>

<details>
<summary> Hint 3 </summary>
<code>v[i][j]</code> can be calculated separately by <b>brute-force</b>. We can create a table of <code>v[i][j]</code> independently to improve the complexity. Also note that semi-palindrome’s length is at least <code>2</code>.
</details>