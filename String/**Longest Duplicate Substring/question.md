# 1044. Longest Duplicate Substring<br> Hard

Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".

Example 1:

<pre>
Input: s = "banana"
Output: "ana"
</pre>

Example 2:

<pre>
Input: s = "abcd"
Output: ""
</pre>

Constraints:

- `2 <= s.length <= 3 * 10^4`
- `s consists of lowercase English letters.`

<details>

<summary> Related Topics </summary>

-   `String`
-   `Hash`

</details>

<details>

<summary> Hint 1 </summary>
Binary search for the length of the answer. (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)
</details>
<details>

<summary> Hint 2 </summary>
To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.
</details>
