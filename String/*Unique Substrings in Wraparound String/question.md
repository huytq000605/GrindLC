# 467. Unique Substrings in Wraparound String<br> Medium

We define the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz", so s will look like this:

"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
Given a string p, return the number of unique non-empty substrings of p are present in s.

Example 1:

<pre>
Input: p = "cac"
Output: 2
Explanation: There are two substrings ("a", "c") of p in s.
</pre>

Example 2:

<pre>
Input: p = "zab"
Output: 6
Explanation: There are six substrings ("z", "a", "b", "za", "ab", and "zab") of p in s.
</pre>

Constraints:

- `1 <= p.length <= 10^5`
- `p consists of lowercase English letters.`

<details>

<summary> Related Topics </summary>

-   `String`
-   `Dynamic Programming`

</details>