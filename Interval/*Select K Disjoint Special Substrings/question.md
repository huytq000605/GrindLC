
# 3458. Select K Disjoint Special Substrings<br> Medium

<p>Given a string <code>s</code> of length <code>n</code> and an integer <code>k</code>, determine whether it is possible to select <code>k</code> disjoint <strong>special substrings</strong>.</p>

<p>A <strong>special substring</strong> is a <span data-keyword="substring-nonempty">substring</span> where:</p>

<ul>
	<li>Any character present inside the substring should not appear outside it in the string.</li>
	<li>The substring is not the entire string <code>s</code>.</li>
</ul>

<p><strong>Note</strong> that all <code>k</code> substrings must be disjoint, meaning they cannot overlap.</p>

<p>Return <code>true</code> if it is possible to select <code>k</code> such disjoint special substrings; otherwise, return <code>false</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abcdbaefab&quot;, k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>We can select two disjoint special substrings: <code>&quot;cd&quot;</code> and <code>&quot;ef&quot;</code>.</li>
	<li><code>&quot;cd&quot;</code> contains the characters <code>&#39;c&#39;</code> and <code>&#39;d&#39;</code>, which do not appear elsewhere in <code>s</code>.</li>
	<li><code>&quot;ef&quot;</code> contains the characters <code>&#39;e&#39;</code> and <code>&#39;f&#39;</code>, which do not appear elsewhere in <code>s</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;cdefdc&quot;, k = 3</span></p>

<p><strong>Output:</strong> <span class="example-io">false</span></p>

<p><strong>Explanation:</strong></p>

<p>There can be at most 2 disjoint special substrings: <code>&quot;e&quot;</code> and <code>&quot;f&quot;</code>. Since <code>k = 3</code>, the output is <code>false</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">s = &quot;abeabe&quot;, k = 0</span></p>

<p><strong>Output:</strong> <span class="example-io">true</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n == s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt;= 26</code></li>
	<li><code>s</code> consists only of lowercase English letters.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Hash Table`
-	`String`
-	`Dynamic Programming`
-	`Greedy`
-	`Sorting`

</details>


<details>
<summary> Hint 1 </summary>
There are at most 26 start points (which are the first occurrence of each letter) and at most 26 end points (which are the last occurrence of each letter) of the substring.
</details>

<details>
<summary> Hint 2 </summary>
Starting from each character, build the smallest special substring interval containing it.
</details>

<details>
<summary> Hint 3 </summary>
Use dynamic programming on the obtained intervals to check if it's possible to pick at least <code>k</code> disjoint intervals.
</details>