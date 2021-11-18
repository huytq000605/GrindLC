# 224. Basic Calculator<br> Hard

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

<pre>
Input: s = " 2-1 + 2 "
Output: 3
</pre>

Example 2:

<pre>
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
</pre>

Constraints:

- `1 <= s.length <= 3 * 10^5`
- `s consists of digits, '+', '-', '(', ')', and ' '.`
- `s represents a valid expression.`
- `'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).`
- `'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).`
- `There will be no two consecutive operators in the input.`
- `Every number and running calculation will fit in a signed 32-bit integer.`

<details>

<summary> Related Topics </summary>

-   `Stack`
-   `Recursive`

</details>