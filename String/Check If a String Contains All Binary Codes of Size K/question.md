# 1461. Check If a String Contains All Binary Codes of Size K<br> Medium

## Given a binary string s and an integer k. Return true if every binary code of length k is a substring of s. Otherwise, return false.



Example 1:

```
Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.:
```

Example 2:

```
Input: s = "00110", k = 2
Output: true:
```

Constraints:

- `1 <= s.length <= 5 * 105`
- `s[i] is either '0' or '1'.`
- `1 <= k <= 20`


<details>

<summary> Related Topics </summary>

-   `Bit wise`
-   `String`

</details>

<details>

<summary> Hint 1 </summary>
We need only to check all sub-strings of length k.
</details>
<details>

<summary> Hint 2 </summary>
The number of distinct sub-strings should be exactly 2^k.
</details>
