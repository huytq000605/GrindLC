# 2062. Count Vowel Substrings of a String<br> Easy

A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.

Example 1:

<pre><strong>Input:</strong> word = "aeiouu"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The vowel substrings of word are as follows (underlined):
- "<strong><u>aeiou</u></strong>u"
- "<strong><u>aeiouu</u></strong>"
</pre>

Example 2:

<pre><strong>Input:</strong> word = "cuaieuouac"
<strong>Output:</strong> 7
<strong>Explanation:</strong> The vowel substrings of word are as follows (underlined):
- "c<strong><u>uaieuo</u></strong>uac"
- "c<strong><u>uaieuou</u></strong>ac"
- "c<strong><u>uaieuoua</u></strong>c"
- "cu<strong><u>aieuo</u></strong>uac"
- "cu<strong><u>aieuou</u></strong>ac"
- "cu<strong><u>aieuoua</u></strong>c"
- "cua<strong><u>ieuoua</u></strong>c"</pre>

Constraints:

- `1 <= word.length <= 100`
- `word consists of lowercase English letters only.`

<details>

<summary> Related Topics </summary>

-   `Sliding Window`

</details>