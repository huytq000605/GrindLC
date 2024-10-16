# 1405. Longest Happy String<br> Medium

A string is called happy if it does not have any of the strings 'aaa', 'bbb' or 'ccc' as a substring.

Given three integers a, b and c, return any string s, which satisfies following conditions:

- s is happy and longest possible.
- s contains at most a occurrences of the letter 'a', at most b occurrences of the letter 'b' and at most c occurrences of the letter 'c'.
- s will only contain 'a', 'b' and 'c' letters.
If there is no such string s return the empty string "".

Example 1:

```
Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
```

Example 2:

```
Input: a = 2, b = 2, c = 1
Output: "aabbc"
```

Constraints:

- `0 <= a, b, c <= 100`
- `a + b + c > 0`

<details>

<summary> Related Topics </summary>

-   `Greedy`

</details>

<details>

<summary> Hint 1 </summary>
Use a greedy approach.
</details>
<details>

<summary> Hint 2 </summary>
Use the letter with the maximum current limit that can be added without breaking the condition.
</details>
