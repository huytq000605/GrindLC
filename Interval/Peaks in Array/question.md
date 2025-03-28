
# 3187. Peaks in Array<br> Hard

<p>A <strong>peak</strong> in an array <code>arr</code> is an element that is <strong>greater</strong> than its previous and next element in <code>arr</code>.</p>

<p>You are given an integer array <code>nums</code> and a 2D integer array <code>queries</code>.</p>

<p>You have to process queries of two types:</p>

<ul>
	<li><code>queries[i] = [1, l<sub>i</sub>, r<sub>i</sub>]</code>, determine the count of <strong>peak</strong> elements in the <span data-keyword="subarray">subarray</span> <code>nums[l<sub>i</sub>..r<sub>i</sub>]</code>.<!-- notionvc: 73b20b7c-e1ab-4dac-86d0-13761094a9ae --></li>
	<li><code>queries[i] = [2, index<sub>i</sub>, val<sub>i</sub>]</code>, change <code>nums[index<sub>i</sub>]</code> to <code><font face="monospace">val<sub>i</sub></font></code>.</li>
</ul>

<p>Return an array <code>answer</code> containing the results of the queries of the first type in order.<!-- notionvc: a9ccef22-4061-4b5a-b4cc-a2b2a0e12f30 --></p>

<p><strong>Notes:</strong></p>

<ul>
	<li>The <strong>first</strong> and the <strong>last</strong> element of an array or a subarray<!-- notionvc: fcffef72-deb5-47cb-8719-3a3790102f73 --> <strong>cannot</strong> be a peak.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [3,1,4,2,5], queries = [[2,3,4],[1,0,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0]</span></p>

<p><strong>Explanation:</strong></p>

<p>First query: We change <code>nums[3]</code> to 4 and <code>nums</code> becomes <code>[3,1,4,4,5]</code>.</p>

<p>Second query: The number of peaks in the <code>[3,1,4,4,5]</code> is 0.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,1,4,2,1,5], queries = [[2,2,4],[1,0,2],[1,0,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,1]</span></p>

<p><strong>Explanation:</strong></p>

<p>First query: <code>nums[2]</code> should become 4, but it is already set to 4.</p>

<p>Second query: The number of peaks in the <code>[4,1,4]</code> is 0.</p>

<p>Third query: The second 4 is a peak in the <code>[4,1,4,2,1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= queries.length &lt;= 10<sup>5</sup></code></li>
	<li><code>queries[i][0] == 1</code> or <code>queries[i][0] == 2</code></li>
	<li>For all <code>i</code> that:
	<ul>
		<li><code>queries[i][0] == 1</code>: <code>0 &lt;= queries[i][1] &lt;= queries[i][2] &lt;= nums.length - 1</code></li>
		<li><code>queries[i][0] == 2</code>: <code>0 &lt;= queries[i][1] &lt;= nums.length - 1</code>, <code>1 &lt;= queries[i][2] &lt;= 10<sup>5</sup></code></li>
	</ul>
	</li>
</ul>


<details>

<summary> Related Topics </summary>

-	`Array`
-	`Binary Indexed Tree`
-	`Segment Tree`

</details>


<details>
<summary> Hint 1 </summary>
Let <code>p[i]</code> be whether <code>nums[i]</code> is a peak in the original array. Namely <code>p[i] = nums[i] > nums[i - 1] && nums[i] > nums[i + 1]</code>.
</details>

<details>
<summary> Hint 2 </summary>
Updating <code>nums[i]</code>, only affects <code>p[i]</code>, <code>p[i - 1]</code> and <code>p[i + 1]</code>. We can recalculate the 3 values in constant time.
</details>

<details>
<summary> Hint 3 </summary>
The answer for <code>[l<sub>i</sub>, r<sub>i</sub>]</code> is <code>p[l<sub>i</sub> + 1] + p[l<sub>i</sub> + 2] + … + p[r<sub>i</sub> - 1]</code> (note that <code>l<sub>i</sub></code> and <code>r<sub>i</sub></code> are not included).
</details>

<details>
<summary> Hint 4 </summary>
Use some data structures (i.e. segment tree or binary indexed tree) to maintain the subarray sum efficiently.
</details>