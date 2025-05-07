
# 3504. Longest Palindrome After Substring Concatenation II<br> Hard

<p>You are given two strings, <code>s</code> and <code>t</code>.</p>

<p>You can create a new string by selecting a <span data-keyword="substring">substring</span> from <code>s</code> (possibly empty) and a substring from <code>t</code> (possibly empty), then concatenating them <strong>in order</strong>.</p>

<p>Return the length of the <strong>longest</strong> <span data-keyword="palindrome-string">palindrome</span> that can be formed this way.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;a&quot;, t = &quot;a&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Concatenating <code>&quot;a&quot;</code> from <code>s</code> and <code>&quot;a&quot;</code> from <code>t</code> results in <code>&quot;aa&quot;</code>, which is a palindrome of length 2.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abc&quot;, t = &quot;def&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">1</span></p>

<p><strong>Explanation:</strong></p>

<p>Since all characters are different, the longest palindrome is any single character, so the answer is 1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;b&quot;, t = &quot;aaaa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Selecting &quot;<code>aaaa</code>&quot; from <code>t</code> is the longest palindrome, so the answer is 4.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abcde&quot;, t = &quot;ecdba&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>Concatenating <code>&quot;abc&quot;</code> from <code>s</code> and <code>&quot;ba&quot;</code> from <code>t</code> results in <code>&quot;abcba&quot;</code>, which is a palindrome of length 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length, t.length &lt;= 1000</code></li>
	<li><code>s</code> and <code>t</code> consist of lowercase English letters.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Two Pointers`
-	`String`
-	`Dynamic Programming`

</details>


<details>
<summary> Hint 1 </summary>
Let <code>dp[i][j]</code> be the length of the longest answer if we try starting it with <code>s[i]</code> and ending it with <code>t[j]</code>.
</details>

<details>
<summary> Hint 2 </summary>
For <code>s</code>, preprocess the length of the longest palindrome starting at index <code>i</code> as <code>p[i]</code>.
</details>

<details>
<summary> Hint 3 </summary>
For <code>t</code>, preprocess the length of the longest palindrome ending at index <code>j</code> as <code>q[j]</code>.
</details>

<details>
<summary> Hint 4 </summary>
If <code>s[i] != t[j]</code>, then <code>dp[i][j] = max(p[i], q[j])</code>.
</details>

<details>
<summary> Hint 5 </summary>
Otherwise, <code>dp[i][j] = max(p[i], q[j], 2 + dp[i + 1][j - 1])</code>.
</details>