
# 1363. Largest Multiple of Three<br> Hard

<p>Given an array of digits <code>digits</code>, return <em>the largest multiple of <strong>three</strong> that can be formed by concatenating some of the given digits in <strong>any order</strong></em>. If there is no answer return an empty string.</p>

<p>Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> digits = [8,1,9]
<strong>Output:</strong> &quot;981&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> digits = [8,6,7,1,0]
<strong>Output:</strong> &quot;8760&quot;
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> digits = [1]
<strong>Output:</strong> &quot;&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= digits.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= digits[i] &lt;= 9</code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Dynamic Programming`
-	`Greedy`

</details>


<details>
<summary> Hint 1 </summary>
A number is a multiple of three if and only if its sum of digits is a multiple of three.
</details>

<details>
<summary> Hint 2 </summary>
Use dynamic programming.
</details>

<details>
<summary> Hint 3 </summary>
To find the maximum number, try to maximize the number of digits of the number.
</details>

<details>
<summary> Hint 4 </summary>
Sort the digits in descending order to find the maximum number.
</details>