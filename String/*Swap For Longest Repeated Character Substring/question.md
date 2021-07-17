# 1156. Swap For Longest Repeated Character Substring<br> Medium

## Given a string text, we are allowed to swap two of the characters in the string. Find the length of the longest substring with repeated characters.



Example 1:

<pre>
Input: text = "ababa"
Output: 3
Explanation: We can swap the first 'b' with the last 'a', or the last 'b' with the first 'a'. Then, the longest repeated character substring is "aaa", which its length is 3.
</pre>

Example 2:

<pre>
Input: text = "aaabaaa"
Output: 6
Explanation: Swap 'b' with the last 'a' (or the first 'a'), and we get longest repeated character substring "aaaaaa", which its length is 6.
</pre>

Constraints:

- `1 <= text.length <= 20000`
- `text consist of lowercase English characters only.`

<details>

<summary> Related Topics </summary>

-   `String`

</details>

<details>

<summary> Hint 1 </summary>
There are two cases: a block of characters, or two blocks of characters between one different character. By keeping a run-length encoded version of the string, we can easily check these cases.
</details>