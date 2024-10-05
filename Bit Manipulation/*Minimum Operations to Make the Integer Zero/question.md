
# 2749. Minimum Operations to Make the Integer Zero<br> Medium

<p>You are given two integers <code>num1</code> and <code>num2</code>.</p>

<p>In one operation, you can choose integer <code>i</code> in the range <code>[0, 60]</code> and subtract <code>2<sup>i</sup> + num2</code> from <code>num1</code>.</p>

<p>Return <em>the integer denoting the <strong>minimum</strong> number of operations needed to make</em> <code>num1</code> <em>equal to</em> <code>0</code>.</p>

<p>If it is impossible to make <code>num1</code> equal to <code>0</code>, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> num1 = 3, num2 = -2
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can make 3 equal to 0 with the following operations:
- We choose i = 2 and substract 2<sup>2</sup> + (-2) from 3, 3 - (4 + (-2)) = 1.
- We choose i = 2 and substract 2<sup>2</sup>&nbsp;+ (-2) from 1, 1 - (4 + (-2)) = -1.
- We choose i = 0 and substract 2<sup>0</sup>&nbsp;+ (-2) from -1, (-1) - (1 + (-2)) = 0.
It can be proven, that 3 is the minimum number of operations that we need to perform.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> num1 = 5, num2 = 7
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be proven, that it is impossible to make 5 equal to 0 with the given operation.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num1 &lt;= 10<sup>9</sup></code></li>
	<li><code><font face="monospace">-10<sup>9</sup>&nbsp;&lt;= num2 &lt;= 10<sup>9</sup></font></code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
If we want to make integer n equal to 0 by only subtracting powers of 2 from n, in how many operations can we achieve it?
</details>

<details>
<summary> Hint 2 </summary>
We need at least - the number of bits in the binary representation of n, and at most - n.
</details>

<details>
<summary> Hint 3 </summary>
Notice that, if it is possible to make num1 equal to 0, then we need at most 60 operations.
</details>

<details>
<summary> Hint 4 </summary>
Iterate on the number of operations.
</details>