
# 2818. Apply Operations to Maximize Score<br> Hard

<p>You are given an array <code>nums</code> of <code>n</code> positive integers and an integer <code>k</code>.</p>

<p>Initially, you start with a score of <code>1</code>. You have to maximize your score by applying the following operation at most <code>k</code> times:</p>

<ul>
	<li>Choose any <strong>non-empty</strong> subarray <code>nums[l, ..., r]</code> that you haven&#39;t chosen previously.</li>
	<li>Choose an element <code>x</code> of <code>nums[l, ..., r]</code> with the highest <strong>prime score</strong>. If multiple such elements exist, choose the one with the smallest index.</li>
	<li>Multiply your score by <code>x</code>.</li>
</ul>

<p>Here, <code>nums[l, ..., r]</code> denotes the subarray of <code>nums</code> starting at index <code>l</code> and ending at the index <code>r</code>, both ends being inclusive.</p>

<p>The <strong>prime score</strong> of an integer <code>x</code> is equal to the number of distinct prime factors of <code>x</code>. For example, the prime score of <code>300</code> is <code>3</code> since <code>300 = 2 * 2 * 3 * 5 * 5</code>.</p>

<p>Return <em>the <strong>maximum possible score</strong> after applying at most </em><code>k</code><em> operations</em>.</p>

<p>Since the answer may be large, return it modulo <code>10<sup>9 </sup>+ 7</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [8,3,9,3,8], k = 2
<strong>Output:</strong> 81
<strong>Explanation:</strong> To get a score of 81, we can apply the following operations:
- Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
It can be proven that 81 is the highest score one can obtain.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [19,12,14,6,10,18], k = 3
<strong>Output:</strong> 4788
<strong>Explanation:</strong> To get a score of 4788, we can apply the following operations: 
- Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
- Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
- Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
It can be proven that 4788 is the highest score one can obtain.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length == n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= k &lt;= min(n * (n + 1) / 2, 10<sup>9</sup>)</code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
<div class="_1l1MA">Calculate <code>nums[i]</code>'s prime score <code>s[i]</code> by factoring in <code>O(sqrt(nums[i]))</code> time.</div>
</details>

<details>
<summary> Hint 2 </summary>
<div class="_1l1MA">For each <code>nums[i]</code>, find the nearest index <code>left[i]</code> on the left (if any) such that <code>s[left[i]] >= s[i]</code>. if none is found, set <code>left[i]</code> to <code>-1</code>. Similarly, find the nearest index <code>right[i]</code> on the right (if any) such that <code>s[right[i]] > s[i]</code>. If none is found, set <code>right[i]</code> to <code>n</code>.</div>
</details>

<details>
<summary> Hint 3 </summary>
<div class="_1l1MA">Use a monotonic stack to compute <code>right[i]</code> and <code>left[i]</code>.</div>
</details>

<details>
<summary> Hint 4 </summary>
<div class="_1l1MA">For each index <code>i</code>, if <code>left[i] + 1 <= l <= i <= r <= right[i] - 1</code>, then <code>s[i]</code> is the maximum value in the range <code>[l, r]</code>. For this particular <code>i</code>, there are <code>ranges[i] = (i - left[i]) * (right[i] - i)</code> ranges where index <code>i</code> will be chosen.</div>
</details>

<details>
<summary> Hint 5 </summary>
<div class="_1l1MA">Loop over all elements of <code>nums</code> by non-increasing prime score, each element will be chosen <code>min(ranges[i], remainingK)</code> times, where <code>reaminingK</code> denotes the number of remaining operations. Therefore, the score will be multiplied by <code>s[i]^min(ranges[i],remainingK)</code>.</div>
</details>

<details>
<summary> Hint 6 </summary>
<div class="_1l1MA">Use fast exponentiation to quickly calculate <code>A^B mod C</code>.</div>
</details>