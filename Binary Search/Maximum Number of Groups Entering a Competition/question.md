
# 2358. Maximum Number of Groups Entering a Competition<br> Medium

<p>You are given a positive integer array <code>grades</code> which represents the grades of students in a university. You would like to enter <strong>all</strong> these students into a competition in <strong>ordered</strong> non-empty groups, such that the ordering meets the following conditions:</p>

<ul>
	<li>The sum of the grades of students in the <code>i<sup>th</sup></code> group is <strong>less than</strong> the sum of the grades of students in the <code>(i + 1)<sup>th</sup></code> group, for all groups (except the last).</li>
	<li>The total number of students in the <code>i<sup>th</sup></code> group is <strong>less than</strong> the total number of students in the <code>(i + 1)<sup>th</sup></code> group, for all groups (except the last).</li>
</ul>

<p>Return <em>the <strong>maximum</strong> number of groups that can be formed</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> grades = [10,6,12,7,3,5]
<strong>Output:</strong> 3
<strong>Explanation:</strong> The following is a possible way to form 3 groups of students:
- 1<sup>st</sup> group has the students with grades = [12]. Sum of grades: 12. Student count: 1
- 2<sup>nd</sup> group has the students with grades = [6,7]. Sum of grades: 6 + 7 = 13. Student count: 2
- 3<sup>rd</sup> group has the students with grades = [10,3,5]. Sum of grades: 10 + 3 + 5 = 18. Student count: 3
It can be shown that it is not possible to form more than 3 groups.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> grades = [8,8]
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can only form 1 group, since forming 2 groups would lead to an equal number of students in both groups.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= grades.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= grades[i] &lt;= 10<sup>5</sup></code></li>
</ul>


<details>

<summary> Related Topics </summary>



</details>


<details>
<summary> Hint 1 </summary>
Would it be easier to place the students into valid groups after sorting them based on their grades in ascending order?
</details>

<details>
<summary> Hint 2 </summary>
Notice that, after sorting, we can separate them into groups of sizes 1, 2, 3, and so on.
</details>

<details>
<summary> Hint 3 </summary>
If the last group is invalid, we can merge it with the previous group.
</details>

<details>
<summary> Hint 4 </summary>
This creates the maximum number of groups because we always greedily form the smallest possible group.
</details>