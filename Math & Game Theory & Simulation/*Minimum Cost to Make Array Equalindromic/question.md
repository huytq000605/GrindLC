
# 2967. Minimum Cost to Make Array Equalindromic<br> Medium

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> having length <code>n</code>.</p>

<p>You are allowed to perform a special move <strong>any</strong> number of times (<strong>including zero</strong>) on <code>nums</code>. In one <strong>special</strong> <strong>move</strong> you perform the following steps <strong>in order</strong>:</p>

<ul>
	<li>Choose an index <code>i</code> in the range <code>[0, n - 1]</code>, and a <strong>positive</strong> integer <code>x</code>.</li>
	<li>Add <code>|nums[i] - x|</code> to the total cost.</li>
	<li>Change the value of <code>nums[i]</code> to <code>x</code>.</li>
</ul>

<p>A <strong>palindromic number</strong> is a positive integer that remains the same when its digits are reversed. For example, <code>121</code>, <code>2552</code> and <code>65756</code> are palindromic numbers whereas <code>24</code>, <code>46</code>, <code>235</code> are not palindromic numbers.</p>

<p>An array is considered <strong>equalindromic</strong> if all the elements in the array are equal to an integer <code>y</code>, where <code>y</code> is a <strong>palindromic number</strong> less than <code>10<sup>9</sup></code>.</p>

<p>Return <em>an integer denoting the <strong>minimum</strong> possible total cost to make </em><code>nums</code><em> <strong>equalindromic</strong> by performing any number of special moves.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4,5]
<strong>Output:</strong> 6
<strong>Explanation:</strong> We can make the array equalindromic by changing all elements to 3 which is a palindromic number. The cost of changing the array to [3,3,3,3,3] using 4 special moves is given by |1 - 3| + |2 - 3| + |4 - 3| + |5 - 3| = 6.
It can be shown that changing all elements to any palindromic number other than 3 cannot be achieved at a lower cost.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,12,13,14,15]
<strong>Output:</strong> 11
<strong>Explanation:</strong> We can make the array equalindromic by changing all elements to 11 which is a palindromic number. The cost of changing the array to [11,11,11,11,11] using 5 special moves is given by |10 - 11| + |12 - 11| + |13 - 11| + |14 - 11| + |15 - 11| = 11.
It can be shown that changing all elements to any palindromic number other than 11 cannot be achieved at a lower cost.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [22,33,22,33,22]
<strong>Output:</strong> 22
<strong>Explanation:</strong> We can make the array equalindromic by changing all elements to 22 which is a palindromic number. The cost of changing the array to [22,22,22,22,22] using 2 special moves is given by |33 - 22| + |33 - 22| = 22.
It can be shown that changing all elements to any palindromic number other than 22 cannot be achieved at a lower cost.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Math`
-	`Greedy`
-	`Sorting`

</details>


<details>
<summary> Hint 1 </summary>
Find the median of <code>nums</code> after sorting it (if the length is even, we can select any number from the two in the middle). Let’s call it <code>m</code>.
</details>

<details>
<summary> Hint 2 </summary>
Try the smallest palindromic number that is larger than or equal to <code>m</code> (if any) and the largest palindromic number that is smaller than or equal to <code>m</code> (if any). These two values are the candidate palindromic numbers for values of all indices.
</details>

<details>
<summary> Hint 3 </summary>
We can use math constructions to construct the two palindromic numbers in <code>O(log(m) / 2)</code> time or we can do it using brute-force by starting from m and checking smaller and larger values in <code>O(sqrt(10<sup>log(m)</sup>))</code>.
</details>

<details>
<summary> Hint 4 </summary>
It is also possible to just generate all palindromic numbers using recursion in <code>O(sqrt(10<sup>9</sup>))</code>.
</details>