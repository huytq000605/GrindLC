# 10. Regular Expression Matching<br> Hard

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

- '.' Matches any single character.​​​​
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:

<pre>
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
</pre>

Example 2:

<pre>
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
</pre>

Example 3:

<pre>
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
</pre>

Example 4:

<pre>
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
</pre>

Example 5:

<pre>
Input: s = "mississippi", p = "mis*is*p*."
Output: false
</pre>

Constraints:

- `1 <= s.length <= 20`
- `1 <= p.length <= 30`
- `s contains only lowercase English letters.`
- `p contains only lowercase English letters, '.', and '*'.`
- `It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`
-   `String`

</details>