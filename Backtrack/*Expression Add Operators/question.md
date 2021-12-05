# 282. Expression Add Operators<br> Hard

Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Example 1:

<pre>
Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
</pre>

Example 2:

<pre>
Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Explanation: Both "1*0+5" and "10-5" evaluate to 5.
Note that "1-05" is not a valid expression because the 5 has a leading zero.
</pre>

Constraints:

- `1 <= num.length <= 10`
- `num consists of only digits.`
- `-2^31 <= target <= 2^31 - 1`

<details>

<summary> Related Topics </summary>

-   `Backtrack`
-   `Recursive`

</details>