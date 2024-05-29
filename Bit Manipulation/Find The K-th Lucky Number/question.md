
# 2802. Find The K-th Lucky Number<br> Medium

<p>We know that <code>4</code> and <code>7</code> are <strong>lucky</strong> digits. Also, a number is called <strong>lucky</strong>&nbsp;if it contains <strong>only</strong> lucky digits.</p>

<p>You are given an integer <code>k</code>, return<em> the </em><code>k<sup>th</sup></code><em>&nbsp;lucky number represented as a <strong>string</strong>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> k = 4
<strong>Output:</strong> &quot;47&quot;
<strong>Explanation:</strong> The first lucky number is 4, the second one is 7, the third one is 44 and the fourth one is 47.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> k = 10
<strong>Output:</strong> &quot;477&quot;
<strong>Explanation:</strong> Here are lucky numbers sorted in increasing order:
4, 7, 44, 47, 74, 77, 444, 447, 474, 477. So the 10<sup>th</sup> lucky number is 477.</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> k = 1000
<strong>Output:</strong> &quot;777747447&quot;
<strong>Explanation:</strong> It can be shown that the 1000<sup>th</sup> lucky number is 777747447.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Math`
-	`String`
-	`Bit Manipulation`

</details>


<details>
<summary> Hint 1 </summary>
<div class="_1l1MA">The number of lucky numbers with <strong>exactly</strong> <code>n</code> digits is equal to <code>2<sup>n</sup></code>.</div>
</details>

<details>
<summary> Hint 2 </summary>
<div class="_1l1MA">We can obtain how many digits the <code>k<sup>th</sup></code> lucky number has.</div>
</details>

<details>
<summary> Hint 3 </summary>
<div class="_1l1MA">Imagine we know that <code>k<sup>th</sup></code> lucky number has <code>c</code> digits. Then calculate how many numbers with <code>c</code> digits exist before the <code>k<sup>th</sup></code> lucky number.</div>
</details>

<details>
<summary> Hint 4 </summary>
<div class="_1l1MA">Imagine the number from the previous hint is <code>x</code>. Now look at the binary representation of <code>x</code> and add some leading zero to make its length equal to <code>c</code>.</div>
</details>

<details>
<summary> Hint 5 </summary>
<div class="_1l1MA">Replace <code>0</code> and <code>1</code> with <code>4</code> and <code>7</code> in the number you've obtained from the previous hint.</div>
</details>