# Array of Doubled Pairs<br> Medium

## Given an array of integers arr of even length, return true if and only if it is possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.

Example 1:

<pre>
Input: arr = [3,1,3,6]
Output: false
</pre>

Example 2:

<pre>
Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
</pre>

Constraints:

- `0 <= arr.length <= 3 * 10^4`
- `arr.length is even.`
- `-10^5 <= arr[i] <= 10^5`

<details>

<summary> Related Topics </summary>

-   `Greedy`
-   `Sorting`

</details>