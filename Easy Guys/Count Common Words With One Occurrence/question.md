# 2085. Count Common Words With One Occurrence<br> Easy

Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.

Example 1:

<pre>
Input: words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
Output: 2
Explanation:
- "leetcode" appears exactly once in each of the two arrays. We count this string.
- "amazing" appears exactly once in each of the two arrays. We count this string.
- "is" appears in each of the two arrays, but there are 2 occurrences of it in words1. We do not count this string.
- "as" appears once in words1, but does not appear in words2. We do not count this string.
Thus, there are 2 strings that appear exactly once in each of the two arrays.
</pre>

Example 2:

<pre>
Input: words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
Output: 0
Explanation: There are no strings that appear in each of the two arrays.
</pre>

Constraints:

- `1 <= words1.length, words2.length <= 1000`
- `1 <= words1[i].length, words2[j].length <= 30`
- `words1[i] and words2[j] consists only of lowercase English letters.`

<details>

<summary> Related Topics </summary>

-   `Array`
-   `Hash Table`

</details>