
# 1696. Jump Game VI<br> Medium

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> and an integer <code>k</code>.</p>

<p>You are initially standing at index <code>0</code>. In one move, you can jump at most <code>k</code> steps forward without going outside the boundaries of the array. That is, you can jump from index <code>i</code> to any index in the range <code>[i + 1, min(n - 1, i + k)]</code> <strong>inclusive</strong>.</p>

<p>You want to reach the last index of the array (index <code>n - 1</code>). Your <strong>score</strong> is the <strong>sum</strong> of all <code>nums[j]</code> for each index <code>j</code> you visited in the array.</p>

<p>Return <em>the <strong>maximum score</strong> you can get</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [<u>1</u>,<u>-1</u>,-2,<u>4</u>,-7,<u>3</u>], k = 2
<strong>Output:</strong> 7
<strong>Explanation:</strong> You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [<u>10</u>,-5,-2,<u>4</u>,0,<u>3</u>], k = 3
<strong>Output:</strong> 17
<strong>Explanation:</strong> You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length, k &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Dynamic Programming`
-	`Queue`
-	`Sliding Window`
-	`Heap (Priority Queue)`
-	`Monotonic Queue`

</details>


<details>
<summary> Hint 1 </summary>
Let dp[i] be "the maximum score to reach the end starting at index i". The answer for dp[i] is nums[i] + max{dp[i+j]} for 1 <= j <= k. That gives an O(n*k) solution.
</details>

<details>
<summary> Hint 2 </summary>
Instead of checking every j for every i, keep track of the largest dp[i] values in a heap and calculate dp[i] from right to left. When the largest value in the heap is out of bounds of the current index, remove it and keep checking.
</details>