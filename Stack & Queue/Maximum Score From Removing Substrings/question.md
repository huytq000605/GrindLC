# 1717. Maximum Score From Removing Substrings<br> Medium

You are given a string s and two integers x and y. You can perform two types of operations any number of times.

<ul>
	<li>Remove substring <code>"ab"</code> and gain <code>x</code> points.
	<ul>
		<li>For example, when removing <code>"ab"</code> from <code>"c<u>ab</u>xbae"</code> it becomes <code>"cxbae"</code>.</li>
	</ul>
	</li>
	<li>Remove substring <code>"ba"</code> and gain <code>y</code> points.
	<ul>
		<li>For example, when removing <code>"ba"</code> from <code>"cabx<u>ba</u>e"</code> it becomes <code>"cabxe"</code>.</li>
	</ul>
	</li>
</ul>

Return the maximum points you can gain after applying the above operations on s.

Example 1:

<pre>
<strong>Input:</strong> s = "cdbcbbaaabab", x = 4, y = 5
<strong>Output:</strong> 19
<strong>Explanation:</strong>
- Remove the "ba" underlined in "cdbcbbaaa<u>ba</u>b". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaa<u>ab</u>". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcb<u>ba</u>a". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbc<u>ba</u>". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
</pre>

Example 2:

<pre>
Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
</pre>

Constraints:

- `1 <= s.length <= 10^5`
- `1 <= x, y <= 10^4`
- `s consists of lowercase English letters.`

<details>

<summary> Related Topics </summary>

-   `Stack`
-   `Greedy`

</details>
