
# 2926. Maximum Balanced Subsequence Sum<br> Hard

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code>.</p>

<p>A <strong>subsequence</strong> of <code>nums</code> having length <code>k</code> and consisting of <strong>indices</strong> <code>i<sub>0</sub>&nbsp;&lt;&nbsp;i<sub>1</sub> &lt;&nbsp;... &lt; i<sub>k-1</sub></code> is <strong>balanced</strong> if the following holds:</p>

<ul>
	<li><code>nums[i<sub>j</sub>] - nums[i<sub>j-1</sub>] &gt;= i<sub>j</sub> - i<sub>j-1</sub></code>, for every <code>j</code> in the range <code>[1, k - 1]</code>.</li>
</ul>

<p>A <strong>subsequence</strong> of <code>nums</code> having length <code>1</code> is considered balanced.</p>

<p>Return <em>an integer denoting the <strong>maximum</strong> possible <strong>sum of elements</strong> in a <strong>balanced</strong> subsequence of </em><code>nums</code>.</p>

<p>A <strong>subsequence</strong> of an array is a new <strong>non-empty</strong> array that is formed from the original array by deleting some (<strong>possibly none</strong>) of the elements without disturbing the relative positions of the remaining elements.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,5,6]
<strong>Output:</strong> 14
<strong>Explanation:</strong> In this example, the subsequence [3,5,6] consisting of indices 0, 2, and 3 can be selected.
nums[2] - nums[0] &gt;= 2 - 0.
nums[3] - nums[2] &gt;= 3 - 2.
Hence, it is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.
The subsequence consisting of indices 1, 2, and 3 is also valid.
It can be shown that it is not possible to get a balanced subsequence with a sum greater than 14.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [5,-1,-3,8]
<strong>Output:</strong> 13
<strong>Explanation:</strong> In this example, the subsequence [5,8] consisting of indices 0 and 3 can be selected.
nums[3] - nums[0] &gt;= 3 - 0.
Hence, it is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.
It can be shown that it is not possible to get a balanced subsequence with a sum greater than 13.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [-2,-1]
<strong>Output:</strong> -1
<strong>Explanation:</strong> In this example, the subsequence [-1] can be selected.
It is a balanced subsequence, and its sum is the maximum among the balanced subsequences of nums.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Binary Search`
-	`Dynamic Programming`
-	`Binary Indexed Tree`
-	`Segment Tree`

</details>


<details>
<summary> Hint 1 </summary>
Let <code>dp[x]</code> represent the maximum sum of a balanced subsequence ending at <code>x</code>.
</details>

<details>
<summary> Hint 2 </summary>
Rewriting the formula <code>nums[i<sub>j</sub>] - nums[i<sub>j-1</sub>] >= i<sub>j</sub> - i<sub>j-1</sub></code> gives <code>nums[i<sub>j</sub>] - i<sub>j</sub> >= nums[i<sub>j-1</sub>] - i<sub>j-1</sub></code>.
</details>

<details>
<summary> Hint 3 </summary>
So, for some index <code>x</code>, we need to find an index <code>y</code>, <code>y < x</code>, such that <code>dp[x] = nums[x] + dp[y]</code> is maximized, and <code>nums[x] - x >= nums[y] - y</code>.
</details>

<details>
<summary> Hint 4 </summary>
There are many ways to achieve this. One method involves sorting the values of <code>nums[x] - x</code> for all indices <code>x</code> and using a segment/Fenwick tree with coordinate compression.
</details>

<details>
<summary> Hint 5 </summary>
Hence, using a dictionary or map, let's call it <code>dict</code>, where <code>dict[nums[x] - x]</code> represents the position of the value, <code>nums[x] - x</code>, in the segment tree.
</details>

<details>
<summary> Hint 6 </summary>
The tree is initialized with zeros initially.
</details>

<details>
<summary> Hint 7 </summary>
For indices <code>x</code> in order from <code>[0, n - 1]</code>, <code>dp[x] = max(nums[x]</code>, <code>nums[x]</code> + the maximum query from the tree in the range <code>[0, dict[nums[x] - x]])</code>, and if <code>dp[x]</code> is greater than the value in the tree at position <code>dict[nums[x] - x]</code>, we update the value in the tree.
</details>

<details>
<summary> Hint 8 </summary>
The answer to the problem is the maximum value in <code>dp</code>.
</details>