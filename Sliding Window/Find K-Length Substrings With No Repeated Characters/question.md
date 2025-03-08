
# 1100. Find K-Length Substrings With No Repeated Characters<br> Medium

<p>Given a string <code>s</code> and an integer <code>k</code>, return <em>the number of substrings in </em><code>s</code><em> of length </em><code>k</code><em> with no repeated characters</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;havefunonleetcode&quot;, k = 5
<strong>Output:</strong> 6
<strong>Explanation:</strong> There are 6 substrings they are: &#39;havef&#39;,&#39;avefu&#39;,&#39;vefun&#39;,&#39;efuno&#39;,&#39;etcod&#39;,&#39;tcode&#39;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;home&quot;, k = 5
<strong>Output:</strong> 0
<strong>Explanation:</strong> Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>4</sup></code></li>
	<li><code>s</code> consists of lowercase English letters.</li>
	<li><code>1 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Hash Table`
-	`String`
-	`Sliding Window`

</details>


<details>
<summary> Hint 1 </summary>
How to check efficiently each K-length substring?
</details>

<details>
<summary> Hint 2 </summary>
First store the first leftmost K-length substring in a hashTable or array of frequencies.
</details>

<details>
<summary> Hint 3 </summary>
Then iterate through the rest of characters and erase the first element and add the next element from the right. If in the hashTable we have K different character we add 1 to the counter. After that return as answer the counter.
</details>