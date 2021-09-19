# 1541. Minimum Insertions to Balance a Parentheses String<br> Medium

Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

- Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
- Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

In other words, we treat '(' as openning parenthesis and '))' as closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

Example 1:

<pre>
Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to to add one more ')' at the end of the string to be "(())))" which is balanced.
</pre>

Example 2:

<pre>
Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
</pre>

Constraints:

- `1 <= s.length <= 10^5`
- `s consists of '(' and ')' only.`

<details>

<summary> Related Topics </summary>

-   `Stack`
-   `String`

</details>
