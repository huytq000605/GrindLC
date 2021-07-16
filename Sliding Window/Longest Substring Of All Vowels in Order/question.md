# 1839. Longest Substring Of All Vowels in Order<br> Medium

A string is considered beautiful if it satisfies the following conditions:

- Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
- The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).

For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.

Example 1:

<pre>
Input: word = "aeiaaio<b>aaaaeiiiiouuu</b>ooaauuaeiu"
Output: 13
Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
</pre>

Example 2:

<pre>
Input: word = "aeeeiiiioooauuu<b>aeiou</b>"
Output: 5
Explanation: The longest beautiful substring in word is "aeiou" of length 5.
</pre>

Constraints:

- `1 <= word.length <= 5 * 10^5`
- `word consists of characters 'a', 'e', 'i', 'o', and 'u'.`

<details>

<summary> Related Topics </summary>

-   `String`
-   `Sliding Window`

</details>