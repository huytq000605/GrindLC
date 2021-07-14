# 1155. Number of Dice Rolls With Target Sum<br> Medium

You have d dice and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 109 + 7 to roll the dice so the sum of the face-up numbers equals target.

Example 1:

```
Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
```

Example 2:

```
Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
```

Constraints:

- `1 <= d, f <= 30`
- `1 <= target <= 1000`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`

</details>
