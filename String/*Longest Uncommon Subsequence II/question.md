# Longest Uncommon Subsequence II<br> Medium

Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).


Example 1:

<pre>
Input: strs = ["aba","cdc","eae"]
Output: 3
</pre>

Example 2:

<pre>
Input: strs = ["aaa","aaa","aa"]
Output: -1
</pre>

Constraints:

- `1 <= strs.length <= 50`
- `1 <= strs[i].length <= 10`
- `strs[i] consists of lowercase English letters.`

<details>

<summary> Related Topics </summary>

-   `String`
-	`Trie`

</details>
