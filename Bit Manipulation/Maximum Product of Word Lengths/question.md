# 318. Maximum Product of Word Lengths<br> Medium

Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.

Example 1:

<pre>
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
</pre>

Example 2:

<pre>
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
</pre>

Constraints:

- `2 <= words.length <= 1000`
- `1 <= words[i].length <= 1000`
- `words[i] consists only of lowercase English letters.`

<details>

<summary> Related Topics </summary>

-   `Bit Manipulation`
-   `String`

</details>