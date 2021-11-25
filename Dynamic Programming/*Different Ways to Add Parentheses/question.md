# 241. Different Ways to Add Parentheses<br> Medium

Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.


Example 1:

<pre>
Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
</pre>

Example 2:

<pre>
Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
</pre>

Constraints:

- `1 <= expression.length <= 20`
- `expression consists of digits and the operator '+', '-', and '*'.`
- `All the integer values in the input expression are in the range [0, 99].`

<details>

<summary> Related Topics </summary>

-   `Dynamic Programming`

</details>