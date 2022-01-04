# 898. Bitwise ORs of Subarrays<br> Medium

We have an array arr of non-negative integers.

For every (contiguous) subarray sub = [arr[i], arr[i + 1], ..., arr[j]] (with i <= j), we take the bitwise OR of all the elements in sub, obtaining a result arr[i] | arr[i + 1] | ... | arr[j].

Return the number of possible results. Results that occur more than once are only counted once in the final answer

Example 1:

<pre>
Input: arr = [0]
Output: 1
Explanation: There is only one possible result: 0.
</pre>

Example 2:

<pre>
Input: arr = [1,1,2]
Output: 3
Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
</pre>

Constraints:

- `1 <= nums.length <= 5 * 10^4`
- `0 <= nums[i] <= 10^9`

<details>

<summary> Related Topics </summary>

-   `Bit Manipulation`

</details>