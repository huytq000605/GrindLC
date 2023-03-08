
# 1055. Shortest Way to Form String<br> Medium

<p>A <strong>subsequence</strong> of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., <code>&quot;ace&quot;</code> is a subsequence of <code>&quot;<u>a</u>b<u>c</u>d<u>e</u>&quot;</code> while <code>&quot;aec&quot;</code> is not).</p>

<p>Given two strings <code>source</code> and <code>target</code>, return <em>the minimum number of <strong>subsequences</strong> of </em><code>source</code><em> such that their concatenation equals </em><code>target</code>. If the task is impossible, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abc&quot;, target = &quot;abcbc&quot;
<strong>Output:</strong> 2
<strong>Explanation:</strong> The target &quot;abcbc&quot; can be formed by &quot;abc&quot; and &quot;bc&quot;, which are subsequences of source &quot;abc&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;abc&quot;, target = &quot;acdbc&quot;
<strong>Output:</strong> -1
<strong>Explanation:</strong> The target string cannot be constructed from the subsequences of source string due to the character &quot;d&quot; in target string.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> source = &quot;xyz&quot;, target = &quot;xzyxz&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> The target string can be constructed as follows &quot;xz&quot; + &quot;y&quot; + &quot;xz&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= source.length, target.length &lt;= 1000</code></li>
	<li><code>source</code> and <code>target</code> consist of lowercase English letters.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Two Pointers`
-	`String`
-	`Greedy`

</details>


<details>
<summary> Hint 1 </summary>
Which conditions have to been met in order to be impossible to form the target string?
</details>

<details>
<summary> Hint 2 </summary>
If there exists a character in the target string which doesn't exist in the source string then it will be impossible to form the target string.
</details>

<details>
<summary> Hint 3 </summary>
Assuming we are in the case which is possible to form the target string, how can we assure the minimum number of used subsequences of source?
</details>

<details>
<summary> Hint 4 </summary>
For each used subsequence try to match the leftmost character of the current subsequence with the leftmost character of the target string, if they match then erase both character otherwise erase just the subsequence character whenever the current subsequence gets empty, reset it to a new copy of subsequence and increment the count, do this until the target sequence gets empty. Finally return the count.
</details>