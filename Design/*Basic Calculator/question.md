# 224. Basic Calculator<br> Medium

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

<pre>
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
</pre>

Example 2:

<pre>
Input: s = " 2-1 + 2 "
Output: 3
</pre>

Constraints:

- `1 <= s.length <= 3 * 10^5`
- `s consists of digits, '+', '-', '(', ')', and ' '.`
- `s represents a valid expression.`
- `'+' is not used as a unary operation.`
- `'-' could be used as a unary operation but it has to be inside parentheses.`
- `There will be no two consecutive operators in the input.`
- `Every number and running calculation will fit in a signed 32-bit integer.`

<details>

<summary> Related Topics </summary>

-   `Math`
-   `String`
-	`Stack`

</details>