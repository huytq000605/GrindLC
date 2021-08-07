# 822. Card Flipping Game<br> Medium

You are given n cards, with a positive integer printed on the front and back of each card (possibly different). You can flip any number of cards (possibly zero).

After choosing the front and the back of each card, you will pick each card, and if the integer printed on the back of this card is not printed on the front of any other card, then this integer is good.

You are given two integer array fronts and backs where fronts[i] and backs[i] are the integers printer on the front and the back of the ith card respectively.

Return the smallest good and integer after flipping the cards. If there are no good integers, return 0.

Note that a flip swaps the front and back numbers, so the value on the front is now on the back and vice versa.


Example 1:

<pre>
Input: fronts = [1,2,4,4,7], backs = [1,3,4,1,3]
Output: 2
Explanation: If we flip the second card, the fronts are [1,3,4,4,7] and the backs are [1,2,4,1,3].
We choose the second card, which has the number 2 on the back, and it is not on the front of any card, so 2 is good.
</pre>

Example 2:

<pre>
Input: fronts = [1], backs = [1]
Output: 0
</pre>

Constraints:

- `n == fronts.length`
- `n == backs.length`
- `1 <= n <= 1000`
- `1 <= fronts[i], backs[i] <= 2000`

<details>

<summary> Related Topics </summary>

-   `Array`
-   `Hash Table`

</details>