# 44. Wildcard Matching<br> Hard

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

- '?' Matches any single character.
- '*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:

<pre>
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
</pre>

Example 2:

<pre>
Input: s = "adceb", p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
</pre>

Constraints:

- `0 <= s.length, p.length <= 2000`
- `s contains only lowercase English letters.`
- `p contains only lowercase English letters, '?' or '*'`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`
-   `String`

</details>