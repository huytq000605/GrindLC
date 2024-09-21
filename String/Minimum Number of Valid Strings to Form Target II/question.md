
# 3292. Minimum Number of Valid Strings to Form Target II<br> Hard

<p>You are given an array of strings <code>words</code> and a string <code>target</code>.</p>

<p>A string <code>x</code> is called <strong>valid</strong> if <code>x</code> is a <span data-keyword="string-prefix">prefix</span> of <strong>any</strong> string in <code>words</code>.</p>

<p>Return the <strong>minimum</strong> number of <strong>valid</strong> strings that can be <em>concatenated</em> to form <code>target</code>. If it is <strong>not</strong> possible to form <code>target</code>, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;abc&quot;,&quot;aaaaa&quot;,&quot;bcdef&quot;], target = &quot;aabcdabc&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>The target string can be formed by concatenating:</p>

<ul>
	<li>Prefix of length 2 of <code>words[1]</code>, i.e. <code>&quot;aa&quot;</code>.</li>
	<li>Prefix of length 3 of <code>words[2]</code>, i.e. <code>&quot;bcd&quot;</code>.</li>
	<li>Prefix of length 3 of <code>words[0]</code>, i.e. <code>&quot;abc&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;abababab&quot;,&quot;ab&quot;], target = &quot;ababaababa&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The target string can be formed by concatenating:</p>

<ul>
	<li>Prefix of length 5 of <code>words[0]</code>, i.e. <code>&quot;ababa&quot;</code>.</li>
	<li>Prefix of length 5 of <code>words[0]</code>, i.e. <code>&quot;ababa&quot;</code>.</li>
</ul>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">words = [&quot;abcdef&quot;], target = &quot;xyz&quot;</span></p>

<p><strong>Output:</strong> <span class="example-io">-1</span></p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 5 * 10<sup>4</sup></code></li>
	<li>The input is generated such that <code>sum(words[i].length) &lt;= 10<sup>5</sup></code>.</li>
	<li><code>words[i]</code> consists only of lowercase English letters.</li>
	<li><code>1 &lt;= target.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>target</code> consists only of lowercase English letters.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`String`
-	`Binary Search`
-	`Dynamic Programming`
-	`Segment Tree`
-	`Rolling Hash`
-	`String Matching`
-	`Hash Function`

</details>


<details>
<summary> Hint 1 </summary>
Let <code>dp[i]</code> be the minimum cost to form the prefix of length <code>i</code> of <code>target</code>.
</details>

<details>
<summary> Hint 2 </summary>
Use Rabin-Karp to hash every prefix and store it in a HashSet.
</details>

<details>
<summary> Hint 3 </summary>
Use Binary search to find the longest substring starting at index <code>i</code> (<code>target[i..j]</code>) that has a hash present in the HashSet.
</details>

<details>
<summary> Hint 4 </summary>
Inverse Modulo precomputation can optimise hash calculation.
</details>

<details>
<summary> Hint 5 </summary>
Use Lazy Segment Tree, or basic Segment Tree to update <code>dp[i..j]</code>.
</details>

<details>
<summary> Hint 6 </summary>
Is it possible to use two TreeSets to update <code>dp[i..j]</code>?
</details>