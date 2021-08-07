# 1759. Count Number of Homogenous Substrings<br> Medium

Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

Example 1:

<pre>
Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.
</pre>

Example 2:

<pre>
Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".
</pre>

Constraints:

- `1 <= s.length <= 10^5`
- `s consists of lowercase letters.`

<details>

<summary> Related Topics </summary>

-   `String`
-   `Math`

</details>