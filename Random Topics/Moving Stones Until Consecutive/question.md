# 1033. Moving Stones Until Consecutive<br> Medium

There are three stones in different positions on the X-axis. You are given three integers a, b, and c, the positions of the stones.

In one move, you pick up a stone at an endpoint (i.e., either the lowest or highest position stone), and move it to an unoccupied position between those endpoints. Formally, let's say the stones are currently at positions x, y, and z with x < y < z. You pick up the stone at either position x or position z, and move that stone to an integer position k, with x < k < z and k != y.

The game ends when you cannot make any more moves (i.e., the stones are in three consecutive positions).

Return an integer array answer of length 2 where:

- answer[0] is the minimum number of moves you can play, and
- answer[1] is the maximum number of moves you can play.

Example 1:

<pre>
Input: a = 1, b = 2, c = 5
Output: [1,2]
Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to 3.
</pre>

Example 2:

<pre>
Input: a = 3, b = 5, c = 1
Output: [1,2]
Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to 4.
</pre>

Constraints:

- `1 <= a, b, c <= 100`
- `a, b, and c have different values.`

<details>

<summary> Related Topics </summary>

-   `Brainteaser`

</details>