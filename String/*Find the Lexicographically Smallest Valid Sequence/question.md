
# 3302. Find the Lexicographically Smallest Valid Sequence<br> Medium

<p>You are given two strings <code>word1</code> and <code>word2</code>.</p>

<p>A string <code>x</code> is called <strong>almost equal</strong> to <code>y</code> if you can change <strong>at most</strong> one character in <code>x</code> to make it <em>identical</em> to <code>y</code>.</p>

<p>A sequence of indices <code>seq</code> is called <strong>valid</strong> if:</p>

<ul>
	<li>The indices are sorted in <strong>ascending</strong> order.</li>
	<li><em>Concatenating</em> the characters at these indices in <code>word1</code> in <strong>the same</strong> order results in a string that is <strong>almost equal</strong> to <code>word2</code>.</li>
</ul>

<p>Return an array of size <code>word2.length</code> representing the <span data-keyword="lexicographically-smaller-array">lexicographically smallest</span> <strong>valid</strong> sequence of indices. If no such sequence of indices exists, return an <strong>empty</strong> array.</p>

<p><strong>Note</strong> that the answer must represent the <em>lexicographically smallest array</em>, <strong>not</strong> the corresponding string formed by those indices.<!-- notionvc: 2ff8e782-bd6f-4813-a421-ec25f7e84c1e --></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = &quot;vbcca&quot;, word2 = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1,2]</span></p>

<p><strong>Explanation:</strong></p>

<p>The lexicographically smallest valid sequence of indices is <code>[0, 1, 2]</code>:</p>

<ul>
	<li>Change <code>word1[0]</code> to <code>&#39;a&#39;</code>.</li>
	<li><code>word1[1]</code> is already <code>&#39;b&#39;</code>.</li>
	<li><code>word1[2]</code> is already <code>&#39;c&#39;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = &quot;bacdc&quot;, word2 = &quot;abc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,4]</span></p>

<p><strong>Explanation:</strong></p>

<p>The lexicographically smallest valid sequence of indices is <code>[1, 2, 4]</code>:</p>

<ul>
	<li><code>word1[1]</code> is already <code>&#39;a&#39;</code>.</li>
	<li>Change <code>word1[2]</code> to <code>&#39;b&#39;</code>.</li>
	<li><code>word1[4]</code> is already <code>&#39;c&#39;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = &quot;aaaaaa&quot;, word2 = &quot;aaabc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[]</span></p>

<p><strong>Explanation:</strong></p>

<p>There is no valid sequence of indices.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">word1 = &quot;abc&quot;, word2 = &quot;ab&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1]</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= word2.length &lt; word1.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>word1</code> and <code>word2</code> consist only of lowercase English letters.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Two Pointers`
-	`String`
-	`Dynamic Programming`
-	`Greedy`

</details>


<details>
<summary> Hint 1 </summary>
Let <code>dp[i]</code> be the longest suffix of <code>word2</code> that exists as a subsequence of suffix of the substring of <code>word1</code> starting at index <code>i</code>.
</details>

<details>
<summary> Hint 2 </summary>
If <code>dp[i + 1] < m</code> and <code>word1[i] == word2[m - dp[i + 1] - 1]</code>,<code>dp[i] =  dp[i + 1] + 1</code>. Otherwise, <code>dp[i] =  dp[i + 1]</code>.
</details>

<details>
<summary> Hint 3 </summary>
For each index <code>i</code>, greedily select characters using the <code>dp</code> array to know whether a solution exists.
</details>