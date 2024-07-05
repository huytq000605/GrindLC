
# 3196. Maximize Total Cost of Alternating Subarrays<br> Medium

<p>You are given an integer array <code>nums</code> with length <code>n</code>.</p>

<p>The <strong>cost</strong> of a <span data-keyword="subarray-nonempty">subarray</span> <code>nums[l..r]</code>, where <code>0 &lt;= l &lt;= r &lt; n</code>, is defined as:</p>

<p><code>cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (&minus;1)<sup>r &minus; l</sup></code></p>

<p>Your task is to <strong>split</strong> <code>nums</code> into subarrays such that the <strong>total</strong> <strong>cost</strong> of the subarrays is <strong>maximized</strong>, ensuring each element belongs to <strong>exactly one</strong> subarray.</p>

<p>Formally, if <code>nums</code> is split into <code>k</code> subarrays, where <code>k &gt; 1</code>, at indices <code>i<sub>1</sub>, i<sub>2</sub>, ..., i<sub>k &minus; 1</sub></code>, where <code>0 &lt;= i<sub>1</sub> &lt; i<sub>2</sub> &lt; ... &lt; i<sub>k - 1</sub> &lt; n - 1</code>, then the total cost will be:</p>

<p><code>cost(0, i<sub>1</sub>) + cost(i<sub>1</sub> + 1, i<sub>2</sub>) + ... + cost(i<sub>k &minus; 1</sub> + 1, n &minus; 1)</code></p>

<p>Return an integer denoting the <em>maximum total cost</em> of the subarrays after splitting the array optimally.</p>

<p><strong>Note:</strong> If <code>nums</code> is not split into subarrays, i.e. <code>k = 1</code>, the total cost is simply <code>cost(0, n - 1)</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,-2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">10</span></p>

<p><strong>Explanation:</strong></p>

<p>One way to maximize the total cost is by splitting <code>[1, -2, 3, 4]</code> into subarrays <code>[1, -2, 3]</code> and <code>[4]</code>. The total cost will be <code>(1 + 2 + 3) + 4 = 10</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,-1,1,-1]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>One way to maximize the total cost is by splitting <code>[1, -1, 1, -1]</code> into subarrays <code>[1, -1]</code> and <code>[1, -1]</code>. The total cost will be <code>(1 + 1) + (1 + 1) = 4</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [0]</span></p>

<p><strong>Output:</strong> 0</p>

<p><strong>Explanation:</strong></p>

<p>We cannot split the array further, so the answer is 0.</p>
</div>

<p><strong class="example">Example 4:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,-1]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Selecting the whole array gives a total cost of <code>1 + 1 = 2</code>, which is the maximum.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Dynamic Programming`

</details>


<details>
<summary> Hint 1 </summary>
The problem can be solved using dynamic programming.
</details>

<details>
<summary> Hint 2 </summary>
Since we can always start a new subarray, the problem is the same as selecting some elements in the array and flipping their signs to negative to maximize the sum. However, we cannot flip the signs of 2 consecutive elements, and the first element in the array cannot be negative.
</details>

<details>
<summary> Hint 3 </summary>
Let <code>dp[i][0/1]</code> be the largest sum we can get for prefix <code>nums[0..i]</code>, where <code>dp[i][0]</code> is the maximum if the <code>i<sup>th</sup></code> element wasn't flipped, and <code>dp[i][1]</code> is the maximum if the <code>i<sup>th</sup></code> element was flipped.
</details>

<details>
<summary> Hint 4 </summary>
Based on the restriction:<br />
<code>dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + nums[i]</code><br />
<code>dp[i][1] = dp[i - 1][0] - nums[i]</code>
</details>

<details>
<summary> Hint 5 </summary>
The initial state is:<br />
<code>dp[1][0] = nums[0] + nums[1]</code><br />
<code>dp[1][1] = nums[0] - nums[1]</code><br />
and the answer is <code>max(dp[n - 1][0], dp[n - 1][1])</code>.
</details>

<details>
<summary> Hint 6 </summary>
Can you optimize the space complexity?
</details>