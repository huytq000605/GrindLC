
# 166. Fraction to Recurring Decimal<br> Medium

<p>Given two integers representing the <code>numerator</code> and <code>denominator</code> of a fraction, return <em>the fraction in string format</em>.</p>

<p>If the fractional part is repeating, enclose the repeating part in parentheses.</p>

<p>If multiple answers are possible, return <strong>any of them</strong>.</p>

<p>It is <strong>guaranteed</strong> that the length of the answer string is less than <code>10<sup>4</sup></code> for all the given inputs.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> numerator = 1, denominator = 2
<strong>Output:</strong> &quot;0.5&quot;
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> numerator = 2, denominator = 1
<strong>Output:</strong> &quot;2&quot;
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> numerator = 4, denominator = 333
<strong>Output:</strong> &quot;0.(012)&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2<sup>31</sup> &lt;=&nbsp;numerator, denominator &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>denominator != 0</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Hash Table`
-	`Math`
-	`String`

</details>


<details>
<summary> Hint 1 </summary>
No scary math, just apply elementary math knowledge. Still remember how to perform a <i>long division</i>?
</details>

<details>
<summary> Hint 2 </summary>
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
</details>

<details>
<summary> Hint 3 </summary>
Notice that once the remainder starts repeating, so does the divided result.
</details>

<details>
<summary> Hint 4 </summary>
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
</details>