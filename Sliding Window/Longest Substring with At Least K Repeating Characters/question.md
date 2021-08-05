# 395. Longest Substring with At Least K Repeating Characters<br> Medium

## Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Example 1:

<pre>
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
</pre>

Example 2:

<pre>
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
</pre>

Constraints:

- `1 <= s.length <= 10^4`
- `s consists of only lowercase English letters.`
- `1 <= k <= 10^5`

<details>

<summary> Related Topics </summary>

-   `Sliding Window`

</details>
