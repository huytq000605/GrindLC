# 1300. Sum of Mutated Array Closest to Target<br> Medium

Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.


Example 1:

<pre>
Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.
</pre>

Example 2:

<pre>
Input: arr = [2,3,5], target = 10
Output: 5
</pre>

Constraints:

- `1 <= arr.length <= 10^4`
- `1 <= arr[i], target <= 10^5`

<details>

<summary> Related Topics </summary>

-   `Binary Search`

</details>
