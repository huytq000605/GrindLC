
# 2561. Rearranging Fruits<br> Hard

<p>You have two fruit baskets containing <code>n</code> fruits each. You are given two <strong>0-indexed</strong> integer arrays <code>basket1</code> and <code>basket2</code> representing the cost of fruit in each basket. You want to make both baskets <strong>equal</strong>. To do so, you can use the following operation as many times as you want:</p>

<ul>
	<li>Chose two indices <code>i</code> and <code>j</code>, and swap the <code>i<sup>th</sup> </code>fruit of <code>basket1</code> with the <code>j<sup>th</sup></code> fruit of <code>basket2</code>.</li>
	<li>The cost of the swap is <code>min(basket1[i],basket2[j])</code>.</li>
</ul>

<p>Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.</p>

<p>Return <em>the minimum cost to make both the baskets equal or </em><code>-1</code><em> if impossible.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> basket1 = [4,2,2,2], basket2 = [1,4,1,2]
<strong>Output:</strong> 1
<strong>Explanation:</strong> Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> basket1 = [2,3,4,1], basket2 = [3,2,5,1]
<strong>Output:</strong> -1
<strong>Explanation:</strong> It can be shown that it is impossible to make both the baskets equal.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>basket1.length == bakste2.length</code></li>
	<li><code>1 &lt;= basket1.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= basket1[i],basket2[i]&nbsp;&lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
Create two frequency maps for both arrays, and find the minimum element among all elements of both arrays.
</details>

<details>
<summary> Hint 2 </summary>
Check if the sum of frequencies of an element in both arrays is odd, if so return -1
</details>

<details>
<summary> Hint 3 </summary>
Store the elements that need to be swapped in a vector, and sort it.
</details>

<details>
<summary> Hint 4 </summary>
Can we reduce swapping cost with the help of minimum element?
</details>

<details>
<summary> Hint 5 </summary>
Calculate the minimum cost of swapping.
</details>