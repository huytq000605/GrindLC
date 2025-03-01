
# 1151. Minimum Swaps to Group All 1's Together<br> Medium

<p>Given a&nbsp;binary array <code>data</code>, return&nbsp;the minimum number of swaps required to group all <code>1</code>&rsquo;s present in the array together in <strong>any place</strong> in the array.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> data = [1,0,1,0,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> There are 3 ways to group all 1&#39;s together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> data = [0,0,0,1,0]
<strong>Output:</strong> 0
<strong>Explanation:</strong> Since there is only one 1 in the array, no swaps are needed.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> data = [1,0,1,0,1,0,0,1,1,0,1]
<strong>Output:</strong> 3
<strong>Explanation:</strong> One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= data.length &lt;= 10<sup>5</sup></code></li>
	<li><code>data[i]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Sliding Window`

</details>


<details>
<summary> Hint 1 </summary>
How many 1's should be grouped together ? Is not a fixed number?
</details>

<details>
<summary> Hint 2 </summary>
Yeah it's just the number of 1's the whole array has. Let's name this number as ones
</details>

<details>
<summary> Hint 3 </summary>
Every subarray of size of ones, needs some number of swaps to reach, Can you find the number of swaps needed to group all 1's in this subarray?
</details>

<details>
<summary> Hint 4 </summary>
It's the number of zeros in that subarray.
</details>

<details>
<summary> Hint 5 </summary>
Do you need to count the number of zeros all over again for every position ?
</details>

<details>
<summary> Hint 6 </summary>
Use Sliding Window technique.
</details>