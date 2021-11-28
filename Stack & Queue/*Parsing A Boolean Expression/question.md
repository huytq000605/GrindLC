# 1106. Parsing A Boolean Expression<br> Hard

Return the result of evaluating a given boolean expression, represented as a string.

An expression can either be:

- "t", evaluating to True;
- "f", evaluating to False;
- "!(expr)", evaluating to the logical NOT of the inner expression expr;
- "&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
- "|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...

Example 1:

<pre>
Input: expression = "!(f)"
Output: true
</pre>

Example 2:

<pre>
Input: expression = "|(&(t,f,t),!(t))"
Output: false
</pre>

Constraints:

- `1 <= expression.length <= 20000`
- `expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.`
- `expression is a valid expression representing a boolean, as given in the description.`

<details>

<summary> Related Topics </summary>

-   `Stack`
-   `String`

</details>