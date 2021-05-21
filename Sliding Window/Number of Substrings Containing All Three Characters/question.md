# 1358. Number of Substrings Containing All Three Characters<br> Medium

## Given a string s consisting only of characters a, b and c. Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:
```
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
```
Example 2:
```
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
 ```

Example 3:
```
Input: s = "abc"
Output: 1
 ```

Constraints:

* `3 <= s.length <= 5 x 10^4`
* `s only consists of a, b or c characters.`

<details>

<summary> Related Topics </summary>

* `Sliding Window` 
* `String`

</details>

<details>

<summary> Hint 1 </summary>
For each position we simply need to find the first occurrence of a/b/c on or after this position.

</details>

<details>

<summary> Hint 2 </summary>
So we can pre-compute three link-list of indices of each a, b, and c.

</details>