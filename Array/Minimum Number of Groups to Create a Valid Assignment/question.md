
# 2910. Minimum Number of Groups to Create a Valid Assignment<br> Medium

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of length <code>n</code>.</p>

<p>We want to group the indices so for each index <code>i</code> in the range <code>[0, n - 1]</code>, it is assigned to <strong>exactly one</strong> group.</p>

<p>A group<strong> </strong>assignment is <strong>valid</strong> if the following conditions hold:</p>

<ul>
	<li>For every group <code>g</code>, all indices <code>i</code> assigned to group <code>g</code> have the same value in <code>nums</code>.</li>
	<li>For any two groups <code>g<sub>1</sub></code> and <code>g<sub>2</sub></code>, the <strong>difference</strong> between the <strong>number of indices</strong> assigned to <code>g<sub>1</sub></code> and <code>g<sub>2</sub></code> should <strong>not exceed</strong> <code>1</code>.</li>
</ul>

<p>Return <em>an integer denoting </em><em>the <strong>minimum</strong> number of groups needed to create a valid group assignment.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,2,3,2,3]
<strong>Output:</strong> 2
<strong>Explanation:</strong> One way the indices can be assigned to 2 groups is as follows, where the values in square brackets are indices:
group 1 -&gt; [0,2,4]
group 2 -&gt; [1,3]
All indices are assigned to one group.
In group 1, nums[0] == nums[2] == nums[4], so all indices have the same value.
In group 2, nums[1] == nums[3], so all indices have the same value.
The number of indices assigned to group 1 is 3, and the number of indices assigned to group 2 is 2.
Their difference doesn&#39;t exceed 1.
It is not possible to use fewer than 2 groups because, in order to use just 1 group, all indices assigned to that group must have the same value.
Hence, the answer is 2.</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [10,10,10,3,1,1]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One way the indices can be assigned to 4 groups is as follows, where the values in square brackets are indices:
group 1 -&gt; [0]
group 2 -&gt; [1,2]
group 3 -&gt; [3]
group 4 -&gt; [4,5]
The group assignment above satisfies both conditions.
It can be shown that it is not possible to create a valid assignment using fewer than 4 groups.
Hence, the answer is 4.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Hash Table`
-	`Greedy`

</details>


<details>
<summary> Hint 1 </summary>
Calculate the frequency of each number.
</details>

<details>
<summary> Hint 2 </summary>
For each <code>x</code> in the range <code>[1, minimum_frequency]</code>, try to create groups with either <code>x</code> or <code>x + 1</code> indices assigned to them while minimizing the total number of groups.
</details>

<details>
<summary> Hint 3 </summary>
For each distinct number, using its frequency, check that all its occurrences can be assigned to groups of size <code>x</code> or <code>x + 1</code> while minimizing the number of groups used.
</details>

<details>
<summary> Hint 4 </summary>
To get the minimum number of groups needed for a number having frequency <code>f</code> to be assigned to groups of size <code>x</code> or <code>x + 1</code>, let <code>a = f / (x + 1)</code> and <code>b = f % (x + 1)</code>. <ul> <li>If <code>b == 0</code>, then we can simply create <code>a</code> groups of size <code>x + 1</code>.</li> <li>If <code>x - b <= a</code>, we can have <code>a - (x - b)</code> groups of size <code>x + 1</code> and <code>x - b + 1</code> groups of size <code>x</code>. So, in total, we have <code>a + 1</code> groups.</li> <li>Otherwise, it's impossible.</li> </ul>
</details>

<details>
<summary> Hint 5 </summary>
The minimum number of groups needed for some <code>x</code> is the total minimized number of groups needed for each distinct number.
</details>

<details>
<summary> Hint 6 </summary>
The answer is the minimum number of groups needed for each <code>x</code> in the range <code>[1, minimum_frequency]</code>.
</details>