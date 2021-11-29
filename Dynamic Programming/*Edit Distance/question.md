# 72. Edit Distance<br> Medium

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

- Insert a character
- Delete a character
- Replace a character

Example 1:

<pre>
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
</pre>

Example 2:

<pre>
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
</pre>

Constraints:

- `0 <= word1.length, word2.length <= 500`
- `word1 and word2 consist of lowercase English letters.`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`

</details>