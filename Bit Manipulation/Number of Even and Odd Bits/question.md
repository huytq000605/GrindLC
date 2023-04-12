
# 2595. Number of Even and Odd Bits<br> Easy

<p>You are given a <strong>positive</strong> integer <code>n</code>.</p>

<p>Let <code>even</code> denote the number of even indices in the binary representation of <code>n</code> (<strong>0-indexed</strong>) with value <code>1</code>.</p>

<p>Let <code>odd</code> denote the number of odd indices in the binary representation of <code>n</code> (<strong>0-indexed</strong>) with value <code>1</code>.</p>

<p>Return <em>an integer array </em><code>answer</code><em> where </em><code>answer = [even, odd]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 17
<strong>Output:</strong> [2,0]
<strong>Explanation:</strong> The binary representation of 17 is 10001. 
It contains 1 on the 0<sup>th</sup> and 4<sup>th</sup> indices. 
There are 2 even and 0 odd indices.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> [0,1]
<strong>Explanation:</strong> The binary representation of 2 is 10.
It contains 1 on the 1<sup>st</sup> index. 
There are 0 even and 1 odd indices.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 1000</code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
Maintain two integer variables, even and odd, to count the number of even and odd indices in the binary representation of integer n.
</details>

<details>
<summary> Hint 2 </summary>
Divide n by 2 while n is positive, and if n modulo 2 is 1, add 1 to its corresponding variable.
</details>